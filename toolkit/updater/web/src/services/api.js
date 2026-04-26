const API_BASE_URL = 'http://127.0.0.1:8080/api';

async function fetchAPI(endpoint, body) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(body),
    });

    let data;
    const text = await response.text();
    try {
      data = text ? JSON.parse(text) : {};
    } catch (err) {
      throw new Error(`[${endpoint}] API returned invalid JSON (Status: ${response.status}). Response: ${text.slice(0, 100)}`);
    }
    
    if (!response.ok) {
      const serverMsg = data.error || 'No error message provided by server';
      throw new Error(`[${endpoint}] API request failed (Status: ${response.status}): ${serverMsg}`);
    }
    
    return data;
  } catch (error) {
    if (error.name === 'TypeError' && error.message === 'Failed to fetch') {
      throw new Error(`[${endpoint}] Network error: Could not connect to the backend server at ${API_BASE_URL}`);
    }
    throw error;
  }
}

export const api = {
  scan: (instance_root) => fetchAPI('/scan', { instance_root }),
  
  initPreview: (instance_root, force = false) => 
    fetchAPI('/init-preview', { instance_root, force }),
    
  initApply: (instance_root, force = false) => 
    fetchAPI('/init-apply', { instance_root, force }),
    
  plan: (instance_root, package_root) => 
    fetchAPI('/plan', { instance_root, package_root }),
    
  apply: (instance_root, package_root) => 
    fetchAPI('/apply', { instance_root, package_root }),
    
  doctor: (instance_root) => fetchAPI('/doctor', { instance_root }),
  
  selectFolder: (title) => fetchAPI('/select-folder', { title }),
};
