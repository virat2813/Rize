import { Routes, Route } from "react-router-dom";

import Home from "./pages/Home";
import Dashboard from "./components/Dashboard";
import QuestsPage from "./pages/QuestsPage";
import StatsPage from "./pages/StatsPage";
import SkillsPage from "./pages/SkillsPage";
import JournalPage from "./pages/JournalPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Home />} />
      <Route path="/dashboard" element={<Dashboard />} />
      <Route path="/quests" element={<QuestsPage />} />
      <Route path="/stats" element={<StatsPage />} />
      <Route path="/skills" element={<SkillsPage />} />
      <Route path="/journal" element={<JournalPage />} />
    </Routes>
  );
}

export default App;