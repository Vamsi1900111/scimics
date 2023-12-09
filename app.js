import React, { useState } from 'react';

const App = () => {
  const [result, setResult] = useState('');

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:5000/get_mcq', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ /* input_data*/ }),
      });

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  };

  return (
    <div>
      <button onClick={fetchData}>Fetch Data</button>
      <pre>{result}</pre>
    </div>
  );
};

export default App;
