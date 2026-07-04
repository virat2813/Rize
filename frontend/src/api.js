const BASE_URL = "http://localhost:8000";

async function handleResponse(response) {
  if (!response.ok) {
    throw new Error(`Request failed with status ${response.status}`);
  }

  return await response.json();
}

export async function getQuests() {
  const response = await fetch(`${BASE_URL}/api/quests`);

  return handleResponse(response);
}

export async function getCharacter() {
  const response = await fetch(`${BASE_URL}/api/character`);

  return handleResponse(response);
}

export async function completeQuest(questId, proofType, proofContent) {
  const formData = new FormData();
  formData.append("proof_type", proofType);
  formData.append("proof_content", proofContent);

  const response = await fetch(
    `${BASE_URL}/api/quests/${questId}/complete`,
    {
      method: "POST",
      body: formData,
    }
  );

  return handleResponse(response);
}

