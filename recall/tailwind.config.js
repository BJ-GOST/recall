/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './recall/templates/**/*.html',
    './accounts/templates/**/*.html',
    './api/templates/**/*.html',
    './recall/static/src/**/*.css',
  ],
  theme: {
    extend: {
      colors:{
        'blue': '#2f2dd1',
        'green':'#79CAD1',
        'teal':'#2FAEB7',
        'yellow':'#eef12a'
      },
    },
  },
  plugins: [],
}

