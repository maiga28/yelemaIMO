module.exports = {
    content: [
        './templates/**/**/*.html',
        './node_modules/flowbite/**/*.js',
        'node_modules/preline/dist/*.js',
        'node_modules/flowbite-react/**/*.{js,jsx,ts,tsx}',

    ],
    theme: {
        extend: {},
    },
    plugins: [
        require('flowbite/plugin'),
        require('preline/plugin'),
    ],
}