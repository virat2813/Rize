import { useEffect, useState } from "react";

function LevelUpOverlay({ newLevel, onDismiss }) {
  const [animate, setAnimate] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      setAnimate(true);
    }, 10);

    return () => clearTimeout(timer);
  }, []);

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-bg-cream/90 backdrop-blur-sm px-6">
      <div className="w-full max-w-md rounded-2xl border border-border-soft bg-card-white p-10 text-center shadow-lg">
        <p className="font-sans text-lg text-text-gray">
          Level
        </p>

        <h1
          className={`mt-3 font-[Manrope] text-7xl font-bold text-primary-green transition-all duration-400 ease-out ${
            animate ? "scale-100 opacity-100" : "scale-75 opacity-0"
          }`}
        >
          {newLevel}
        </h1>

        <div className="mt-6 flex justify-center">
          <div className="h-1.5 w-40 overflow-hidden rounded-full bg-border-soft">
            <div
              className={`h-full bg-accent-gold transition-all duration-400 ease-out ${
                animate ? "w-full" : "w-0"
              }`}
            />
          </div>
        </div>

        <button
          type="button"
          onClick={onDismiss}
          className="mt-10 rounded-xl bg-primary-green px-8 py-3 font-medium text-white transition-colors hover:opacity-90"
        >
          Continue
        </button>
      </div>
    </div>
  );
}

export default LevelUpOverlay;
