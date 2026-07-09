import { useEffect, useState } from "react";
import {
  getCharacter,
  getStreaks,
} from "../api";

const stats = [
  { key: "confidence", label: "Confidence", color: "#D97757" },
  { key: "knowledge", label: "Knowledge", color: "#4F7CAC" },
  { key: "fitness", label: "Fitness", color: "#5E8C61" },
  { key: "creativity", label: "Creativity", color: "#8E7CC3" },
  { key: "social", label: "Social", color: "#D9A441" },
];

function StatBars({ refreshCounter }) {
  const [character, setCharacter] = useState(null);
  const [streaks, setStreaks] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadData() {
      try {
        const [characterData, streakData] =
          await Promise.all([
            getCharacter(),
            getStreaks(),
          ]);

        setCharacter(characterData);
        setStreaks(streakData);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, [refreshCounter]);

  if (loading) {
    return (
      <p className="font-inter text-[#6B7280]">
        Loading stats...
      </p>
    );
  }

  return (
    <div className="space-y-5">
      {stats.map((stat) => {
        const value = character?.[stat.key] ?? 0;
        const percentage = Math.min(value, 100);

        const streak = streaks.find(
          (item) => item.stat_name === stat.key
        );

        return (
          <div key={stat.key}>
            <div className="flex items-center gap-4">
              <div className="w-28">
                <span className="font-inter text-sm text-[#2B2B2B]">
                  {stat.label}
                </span>
              </div>

              <div className="flex flex-1 items-center gap-3">
                <div className="h-3 flex-1 overflow-hidden rounded-full bg-[#E7E2D8]">
                  <div
                    className="h-full rounded-full transition-all duration-500"
                    style={{
                      width: `${percentage}%`,
                      backgroundColor: stat.color,
                    }}
                  />
                </div>

                <span className="w-10 text-right font-inter text-sm text-[#6B7280]">
                  {value}
                </span>
              </div>
            </div>

            {streak && streak.current_streak > 0 && (
              <div className="ml-28 mt-1">
                <p className="font-inter text-xs text-[#6B7280]">
                  {streak.current_streak} day streak
                </p>
              </div>
            )}
          </div>
        );
      })}
    </div>
  );
}

export default StatBars;