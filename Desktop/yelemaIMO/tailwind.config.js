module.exports = {
    content: [
        './templates/**/**/*.html',
        './node_modules/flowbite/**/*.js',
        'node_modules/preline/dist/*.js',

    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin'),
        require('preline/plugin'),
    ],
}