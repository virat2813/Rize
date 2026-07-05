import { useMemo, useState } from "react";
import { completeQuest } from "../api";

function CompleteQuestModal({
  quest,
  onClose,
  onSuccess,
}) {
  const [proofType, setProofType] = useState("photo");
  const [photoFile, setPhotoFile] = useState(null);
  const [textProof, setTextProof] = useState("");

  const [submitting, setSubmitting] = useState(false);
  const [error, setError] = useState("");

  const [completed, setCompleted] = useState(false);
  const [xpEarned, setXpEarned] = useState(0);
  const [narration, setNarration] = useState("");

  const imagePreview = useMemo(() => {
    if (!photoFile) {
      return null;
    }

    return URL.createObjectURL(photoFile);
  }, [photoFile]);

  const canSubmit =
    proofType === "photo"
      ? photoFile !== null
      : textProof.trim().length >= 10;

  function handlePhotoChange(event) {
    setError("");

    if (!event.target.files.length) {
      setPhotoFile(null);
      return;
    }

    setPhotoFile(event.target.files[0]);
  }

  async function handleSubmit() {
    if (!canSubmit || submitting) {
      return;
    }

    setSubmitting(true);
    setError("");

    try {
      const result = await completeQuest(
        quest.id,
        proofType,
        proofType === "photo"
          ? photoFile
          : textProof.trim()
      );

      setXpEarned(quest.xp_reward);
      setNarration(result.ai_narration || "");

      setCompleted(true);
    } catch (err) {
      setError(err.message);
    } finally {
      setSubmitting(false);
    }
  }

  if (completed) {
    return (
      <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">
        <div className="w-full max-w-md rounded-xl bg-white p-8 shadow-xl">

          <h2 className="font-manrope text-2xl font-semibold text-[#2B2B2B]">
            Quest Completed
          </h2>

          <p className="mt-6 font-inter text-lg font-medium text-[#3E7B5D]">
            +{xpEarned} XP
          </p>

          <p className="mt-4 font-inter leading-7 text-[#555]">
            {narration}
          </p>

          <button
            onClick={onSuccess}
            className="mt-8 w-full rounded-lg bg-[#3E7B5D] py-3 font-inter font-medium text-white transition hover:bg-[#35694f]"
          >
            Done
          </button>

        </div>
      </div>
    );
  }

  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-black/40">

      <div className="w-full max-w-md rounded-xl bg-white p-7 shadow-xl">

        <div className="flex items-start justify-between">

          <div>

            <h2 className="font-manrope text-xl font-semibold text-[#2B2B2B]">
              {quest.title}
            </h2>

            <p className="mt-2 font-inter text-sm leading-6 text-[#6B7280]">
              {quest.description}
            </p>

          </div>

          <button
            onClick={onClose}
            className="text-xl text-[#888] hover:text-[#222]"
          >
            ×
          </button>

        </div>

        <div className="mt-6 flex rounded-lg bg-[#F5F3EE] p-1">

          <button
            onClick={() => {
              setProofType("photo");
              setError("");
            }}
            className={`flex-1 rounded-md py-2 font-inter text-sm transition ${
              proofType === "photo"
                ? "bg-[#3E7B5D] text-white"
                : "text-[#555]"
            }`}
          >
            Photo
          </button>

          <button
            onClick={() => {
              setProofType("text");
              setError("");
            }}
            className={`flex-1 rounded-md py-2 font-inter text-sm transition ${
              proofType === "text"
                ? "bg-[#3E7B5D] text-white"
                : "text-[#555]"
            }`}
          >
            Text
          </button>

        </div>
                {proofType === "photo" ? (
          <div className="mt-6">

            {imagePreview && (
              <img
                src={imagePreview}
                alt="Preview"
                className="mb-4 h-48 w-full rounded-lg border border-[#E7E2D8] object-cover"
              />
            )}

            <input
              type="file"
              accept="image/*"
              onChange={handlePhotoChange}
              className="w-full rounded-lg border border-[#E7E2D8] p-2 font-inter text-sm"
            />

          </div>
        ) : (
          <div className="mt-6">

            <textarea
              value={textProof}
              onChange={(event) => {
                setTextProof(event.target.value);
                setError("");
              }}
              rows={6}
              placeholder="Describe how you completed this quest..."
              className="w-full resize-none rounded-lg border border-[#E7E2D8] p-3 font-inter text-sm outline-none transition focus:border-[#3E7B5D]"
            />

            <p className="mt-2 text-right font-inter text-xs text-[#777]">
              {textProof.trim().length}/10 minimum characters
            </p>

          </div>
        )}

        {error && (
          <p className="mt-4 font-inter text-sm text-red-600">
            {error}
          </p>
        )}

        <button
          onClick={handleSubmit}
          disabled={!canSubmit || submitting}
          className={`mt-6 w-full rounded-lg py-3 font-inter font-medium transition ${
            !canSubmit || submitting
              ? "cursor-not-allowed bg-[#AFC6B7] text-white"
              : "bg-[#3E7B5D] text-white hover:bg-[#35694F]"
          }`}
        >
          {submitting ? "Verifying" : "Submit Proof"}
        </button>

      </div>

    </div>
  );
}

export default CompleteQuestModal;
