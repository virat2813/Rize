/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}"
  ],
  theme: {
    extend: {
      colors: {
        "bg-cream": "#FAF8F3",
        "card-white": "#FFFFFF",
        "border-soft": "#E7E2D8",
        "primary-green": "#3E7B5D",
        "secondary-blue": "#5B7DB1",
        "accent-gold": "#D6A84F",
        "text-charcoal": "#2B2B2B",
        "text-gray": "#6B7280",
        "stat-confidence": "#D97757",
        "stat-knowledge": "#4F7CAC",
        "stat-fitness": "#5E8C61",
        "stat-creativity": "#8E7CC3",
        "stat-social": "#D9A441"
      }
    }
  },
  plugins: []
}
