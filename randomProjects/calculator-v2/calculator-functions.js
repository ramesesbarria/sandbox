// Calculator State
const state = {
    current: '0',
    previous: '',
    operator: null,
    shouldResetScreen: false,
    expression: '',
};

// DOM
const resultEl = document.getElementById('result');
const expressionEl = document.getElementById('expression');

// Update display
function updateDisplay() {
    resultEl.textContent = formatNumber(state.current);
    expressionEl.textContent = state.expression;
}

// Format large/small numbers nicely
function formatNumber(val) {
    if (val === 'Error') return 'Error';
    const num = parseFloat(val);
    if (isNaN(num)) return val;
    // Use exponential for very large/small
    if (Math.abs(num) >= 1e12 || (Math.abs(num) < 1e-6 && num !== 0)) {
        return num.toExponential(4);
    }
    // Limit decimal display
    const str = parseFloat(num.toPrecision(10)).toString();
    return str;
}

// Pop animation on result
function popDisplay() {
    resultEl.classList.remove('pop', 'error');
    void resultEl.offsetWidth;
    resultEl.classList.add('pop');
    setTimeout(() => resultEl.classList.remove('pop'), 150);
}

// Handle number input
function inputDigit(digit) {
    if (state.shouldResetScreen) {
        state.current = digit === '.' ? '0.' : digit;
        state.shouldResetScreen = false;
    } else {
        if (digit === '.' && state.current.includes('.')) return;
        if (state.current === '0' && digit !== '.') {
            state.current = digit;
        } else {
            if (state.current.replace('-', '').replace('.', '').length >= 12) return;
            state.current += digit;
        }
    }
    updateDisplay();
}

// Handle operator
function inputOperator(op) {
    // Remove active class from all op buttons
    document.querySelectorAll('.btn-op').forEach(b => b.classList.remove('active-op'));

    if (state.operator && !state.shouldResetScreen) {
        calculate();
    }

    state.previous = state.current;
    state.operator = op;
    state.shouldResetScreen = true;

    const opSymbols = { '+': '+', '-': '−', '*': '×', '/': '÷' };
    state.expression = `${formatNumber(state.previous)} ${opSymbols[op] || op}`;
    updateDisplay();

    // Highlight active op
    document.querySelectorAll('.btn-op').forEach(b => {
        if (b.dataset.value === op) b.classList.add('active-op');
    });
}

// Core calculation
function calculate() {
    if (!state.operator || state.shouldResetScreen) return;

    const prev = parseFloat(state.previous);
    const curr = parseFloat(state.current);
    const opSymbols = { '+': '+', '-': '−', '*': '×', '/': '÷' };
    let result;

    switch (state.operator) {
        case '+': result = prev + curr; break;
        case '-': result = prev - curr; break;
        case '*': result = prev * curr; break;
        case '/':
            if (curr === 0) {
                state.current = 'Error';
                state.expression = '';
                state.operator = null;
                state.shouldResetScreen = true;
                resultEl.classList.add('error');
                expressionEl.textContent = '';
                resultEl.textContent = 'Error';
                return;
            }
            result = prev / curr;
            break;
        default: return;
    }

    state.expression = `${formatNumber(state.previous)} ${opSymbols[state.operator] || state.operator} ${formatNumber(state.current)} =`;
    state.current = parseFloat(result.toPrecision(12)).toString();
    state.operator = null;
    state.shouldResetScreen = true;

    document.querySelectorAll('.btn-op').forEach(b => b.classList.remove('active-op'));
    popDisplay();
    updateDisplay();
}

// Clear all
function clearAll() {
    state.current = '0';
    state.previous = '';
    state.operator = null;
    state.shouldResetScreen = false;
    state.expression = '';
    resultEl.classList.remove('error');
    document.querySelectorAll('.btn-op').forEach(b => b.classList.remove('active-op'));
    updateDisplay();
}

// Toggle sign
function toggleSign() {
    if (state.current === '0' || state.current === 'Error') return;
    state.current = state.current.startsWith('-')
        ? state.current.slice(1)
        : '-' + state.current;
    updateDisplay();
}

// Percent
function percent() {
    if (state.current === 'Error') return;
    state.current = (parseFloat(state.current) / 100).toString();
    updateDisplay();
}

// Button click handler
document.querySelector('.buttons').addEventListener('click', (e) => {
    const btn = e.target.closest('.btn');
    if (!btn) return;

    const { action, value } = btn.dataset;

    if (value !== undefined) {
        if (['+', '-', '*', '/'].includes(value)) {
            inputOperator(value);
        } else {
            inputDigit(value);
        }
    } else if (action) {
        switch (action) {
            case 'clear':   clearAll();     break;
            case 'sign':    toggleSign();   break;
            case 'percent': percent();      break;
            case 'equals':  calculate();    break;
        }
    }
});

// Keyboard support
document.addEventListener('keydown', (e) => {
    if (e.key >= '0' && e.key <= '9') inputDigit(e.key);
    else if (e.key === '.') inputDigit('.');
    else if (e.key === '+') inputOperator('+');
    else if (e.key === '-') inputOperator('-');
    else if (e.key === '*') inputOperator('*');
    else if (e.key === '/') { e.preventDefault(); inputOperator('/'); }
    else if (e.key === 'Enter' || e.key === '=') calculate();
    else if (e.key === 'Escape') clearAll();
    else if (e.key === 'Backspace') {
        if (state.current.length > 1) {
            state.current = state.current.slice(0, -1);
        } else {
            state.current = '0';
        }
        updateDisplay();
    }
});

// Init
updateDisplay();