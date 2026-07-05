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

export async function completeQuest(
  questId,
  proofType,
  proofValue
) {
  const formData = new FormData();

  formData.append("proof_type", proofType);

  if (proofType === "photo") {
    formData.append("proof_photo", proofValue);
  } else {
    formData.append("proof_text", proofValue);
  }

  const response = await fetch(
    `${BASE_URL}/api/quests/${questId}/complete`,
    {
      method: "POST",
      body: formData,
    }
  );

  if (!response.ok) {
    let errorMessage = "Request failed.";

    try {
      const error = await response.json();
      errorMessage = error.detail || errorMessage;
    } catch {
      // Ignore JSON parsing errors
    }

    throw new Error(errorMessage);
  }

  return await response.json();
}