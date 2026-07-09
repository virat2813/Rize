import { useEffect, useState } from "react";

const statColors = {
  confidence: "#D97757",
  knowledge: "#4F7CAC",
  fitness: "#5E8C61",
  creativity: "#8E7CC3",
  social: "#D9A441",
};

const statOrder = [
  "confidence",
  "knowledge",
  "fitness",
  "creativity",
  "social",
];

function SkillTree() {
  const [skills, setSkills] = useState([]);

  useEffect(() => {
    async function loadSkills() {
      try {
        const response = await fetch("http://127.0.0.1:8000/api/skills");
        const data = await response.json();
        setSkills(data);
      } catch (error) {
        console.error("Failed to load skills:", error);
      }
    }

    loadSkills();
  }, []);

  const groupedSkills = {};

  statOrder.forEach((stat) => {
    groupedSkills[stat] = [];
  });

  skills.forEach((skill) => {
    if (groupedSkills[skill.stat_name]) {
      groupedSkills[skill.stat_name].push(skill);
    }
  });

  return (
    <div className="grid grid-cols-1 gap-6 md:grid-cols-2 xl:grid-cols-5">
      {statOrder.map((stat) => (
        <div
          key={stat}
          className="rounded-xl border border-[#E7E2D8] bg-white p-4 shadow-sm"
        >
          <h3
            className="mb-4 font-manrope text-lg font-semibold capitalize"
            style={{ color: statColors[stat] }}
          >
            {stat}
          </h3>

          <div className="space-y-3">
            {groupedSkills[stat].map((skill) => (
              <div
                key={skill.id}
                className={`rounded-lg border border-[#E7E2D8] p-3 transition ${
                  skill.unlocked ? "opacity-100" : "opacity-50"
                }`}
              >
                <div className="flex items-center justify-between">
                  <h4 className="font-inter font-semibold text-[#2B2B2B]">
                    {skill.title}
                  </h4>

                  {skill.unlocked && (
                    <div className="h-3 w-3 rounded-full bg-[#D6A84F]" />
                  )}
                </div>

                {skill.unlocked ? (
                  <p className="mt-2 text-sm text-[#6B7280]">
                    {skill.description}
                  </p>
                ) : (
                  <>
                    <p className="mt-2 text-sm text-[#6B7280]">
                      Unlocks at Level {skill.unlock_level}
                    </p>

                    <span className="mt-2 inline-block text-xs font-medium text-gray-500">
                      Locked
                    </span>
                  </>
                )}
              </div>
            ))}
          </div>
        </div>
      ))}
    </div>
  );
}

export default SkillTree;