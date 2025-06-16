import logo from './logo.svg';
import { useState } from "react";
import './App.css';

function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    setLoading(true);
    setResponse("");
    try {
      const res = await fetch("http://localhost:8000/generate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: prompt }),
      });
      const data = await res.json();
      setResponse(data.response);
    } catch (err) {
      setResponse("Error: " + err.message);
    }
    setLoading(false);
  };

  return (
    <div className="App">
      <h1>Shakespeare Bot</h1>
      <textarea
        rows="5"
        cols="50"
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
        placeholder="Enter your prompt..."
      />
      <br />
      <button onClick={handleSubmit} disabled={loading || !prompt.trim()}>
        {loading ? "Generating..." : "Generate"}
      </button>
      <div style={{ minHeight: "2em", marginTop: "1em" }}>
        {loading && <span>Shakespeare is writing...</span>}
        {!loading && response && (
          <div>
            <strong>Shakespeare says:</strong>
            <div
              style={{ marginTop: "1em", whiteSpace: "pre-wrap" }}
            >
              {response}
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;