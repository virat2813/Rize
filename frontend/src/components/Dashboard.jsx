import { useState } from "react";
import Journal from "./Journal";
import QuestList from "./QuestList";
import StatBars from "./StatBars";
import SkillTree from "./SkillTree";

function Dashboard() {
  const [refreshCounter, setRefreshCounter] = useState(0);

  function handleQuestCompleted() {
    setRefreshCounter((previous) => previous + 1);
  }

  return (
    <div className="min-h-screen bg-[#FAF8F3]">
      <div className="mx-auto max-w-5xl px-6 py-10">
        <p className="font-inter text-lg text-[#6B7280]">
          Good Morning, Virat
        </p>

        <h1 className="mt-2 font-manrope text-5xl font-bold text-[#3E7B5D]">
          Level 1
        </h1>

        <div className="my-8 border-t border-[#E7E2D8]" />

        <section>
          <h2 className="font-manrope text-2xl font-semibold text-[#2B2B2B]">
            Today's Quests
          </h2>

          <div className="mt-4 rounded-xl border border-[#E7E2D8] bg-white p-6 shadow-sm">
            <QuestList onQuestCompleted={handleQuestCompleted} />
          </div>
        </section>

        <div className="my-8 border-t border-[#E7E2D8]" />

        <section>
          <h2 className="font-manrope text-2xl font-semibold text-[#2B2B2B]">
            Your Stats
          </h2>

          <div className="mt-4 rounded-xl border border-[#E7E2D8] bg-white p-6 shadow-sm">
            <StatBars refreshCounter={refreshCounter} />
          </div>
        </section>

        <div className="my-8 border-t border-[#E7E2D8]" />

        <section>
          <h2 className="font-manrope text-2xl font-semibold text-[#2B2B2B]">
            Adventure Journal
          </h2>

          <Journal />
        </section>

        <div className="my-8 border-t border-[#E7E2D8]" />

        <section>
          <h2 className="font-manrope text-2xl font-semibold text-[#2B2B2B]">
            Skills
          </h2>

          <div className="mt-4">
            <SkillTree />
          </div>
        </section>
      </div>
    </div>
  );
}

export default Dashboard;
