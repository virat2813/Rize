import { useEffect, useState } from "react";
import { getQuests } from "../api";
import CompleteQuestModal from "./CompleteQuestModal";

const statColors = {
  Confidence: "bg-[#D97757] text-white",
  Knowledge: "bg-[#4F7CAC] text-white",
  Fitness: "bg-[#5E8C61] text-white",
  Creativity: "bg-[#8E7CC3] text-white",
  Social: "bg-[#D9A441] text-white",
};

function QuestList({ onQuestCompleted }) {
  const [quests, setQuests] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedQuest, setSelectedQuest] = useState(null);

  useEffect(() => {
    async function loadQuests() {
      try {
        const data = await getQuests();
        setQuests(data);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadQuests();
  }, []);

  function handleSuccess() {
    if (onQuestCompleted) {
      onQuestCompleted();
    }

    setSelectedQuest(null);
  }

  if (loading) {
    return (
      <p className="font-inter text-[#6B7280]">
        Loading quests...
      </p>
    );
  }

  return (
    <>
      <div className="space-y-4">
        {quests.map((quest) => {
          const statClass =
            statColors[quest.linked_stat] ||
            "bg-[#6B7280] text-white";

          return (
            <div
              key={quest.id}
              className="cursor-pointer rounded-xl border border-[#E7E2D8] bg-white p-5 shadow-sm transition-shadow hover:shadow-md"
              onClick={() => setSelectedQuest(quest)}
            >
              <div className="flex items-start justify-between gap-4">
                <div>
                  <h3 className="font-manrope text-lg font-semibold text-[#2B2B2B]">
                    {quest.title}
                  </h3>

                  <p className="mt-2 font-inter text-sm text-[#6B7280]">
                    {quest.description}
                  </p>

                  <div className="mt-3">
                    <span
                      className={`inline-flex rounded-full px-3 py-1 text-sm font-medium ${statClass}`}
                    >
                      {quest.linked_stat}
                    </span>
                  </div>
                </div>

                <p className="whitespace-nowrap font-inter text-sm text-[#6B7280]">
                  {quest.xp_reward} XP
                </p>
              </div>
            </div>
          );
        })}
      </div>

      {selectedQuest && (
        <CompleteQuestModal
          quest={selectedQuest}
          onClose={() => setSelectedQuest(null)}
          onSuccess={handleSuccess}
        />
      )}
    </>
  );
}

export default QuestList;