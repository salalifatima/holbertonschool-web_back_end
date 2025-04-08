module.exports = {
    env: {
        browser: false, // Brauzer mühiti istifadə edilmir
        es6: true,      // ES6 xüsusiyyətləri aktiv
        jest: true,     // Jest mühiti aktiv
        node: true      // Node.js mühiti aktiv
    },
    extends: [
        'airbnb-base',
        'plugin:jest/all',
    ],
    globals: {
        Atomics: 'readonly',
        SharedArrayBuffer: 'readonly',
        module: 'readonly', // module dəyişənini tanıyın
    },
    parserOptions: {
        ecmaVersion: 2018,
        sourceType: 'module',
    },
    plugins: ['jest'],
    rules: {
        'no-console': 'off',
        'no-shadow': 'off',
        'no-restricted-syntax': [
            'error',
            'LabeledStatement',
            'WithStatement',
        ],
    },
    overrides: [
        {
            files: ['*.js'],
            excludedFiles: 'babel.config.js',
        }
    ]
};

