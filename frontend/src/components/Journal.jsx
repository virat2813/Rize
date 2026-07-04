import { useEffect, useState } from "react";
import { getCharacter } from "../api";

function Journal() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function loadCharacter() {
      try {
        await getCharacter();
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }

    loadCharacter();
  }, []);

  if (loading) {
    return (
      <p className="font-inter text-[#6B7280]">
        Loading journal...
      </p>
    );
  }

  return (
    <div className="rounded-xl border border-[#E7E2D8] bg-white p-6 shadow-sm">
      {/* This placeholder will be replaced with real completion history in Phase 6. */}
      <p className="font-inter text-[#6B7280]">
        Your completed quests will appear here
      </p>
    </div>
  );
}

export default Journal;
