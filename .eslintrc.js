// Copyright (C) 2021 Ibrahem Mouhamad

module.exports = {
    env: {
        node: true,
        browser: true,
        es6: true,
    },
    parserOptions: {
        sourceType: 'module',
        ecmaVersion: 2018,
    },
    plugins: ['eslint-plugin-header'],
    extends: ['eslint:recommended', 'prettier'],
    rules: {
        'header/header': [2, 'line', [{
            pattern: ' {1}Copyright \\(C\\) 2021 Ibrahem Mouhamad',
            template: ' Copyright (C) 2021 Ibrahem Mouhamad'
        }, '']],
    },
};
