import { useState } from 'react';
import ScanStep from './components/ScanStep';
import InitStep from './components/InitStep';
import PlanStep from './components/PlanStep';
import StatusStep from './components/StatusStep';

export default function App() {
  const [currentStep, setCurrentStep] = useState('scan');
  const [context, setContext] = useState({});
  const [history, setHistory] = useState(['scan']);

  const handleNext = (step, newContextData) => {
    setContext(prev => ({ ...prev, ...newContextData }));
    setHistory(prev => [...prev, step]);
    setCurrentStep(step);
  };

  const handleBack = () => {
    if (history.length > 1) {
      const newHistory = [...history];
      newHistory.pop();
      const prevStep = newHistory[newHistory.length - 1];
      setHistory(newHistory);
      setCurrentStep(prevStep);
    }
  };

  const handleRestart = () => {
    setContext({});
    setHistory(['scan']);
    setCurrentStep('scan');
  };

  return (
    <>
      <header style={{ textAlign: 'center', marginBottom: '2rem' }}>
        <h1>RAIDEN Installer</h1>
        <p>Local managed core updater</p>
      </header>

      <main>
        {currentStep === 'scan' && (
          <ScanStep context={context} onNext={handleNext} />
        )}
        
        {currentStep === 'init' && (
          <InitStep 
            context={context} 
            onNext={handleNext} 
            onBack={handleBack} 
          />
        )}
        
        {currentStep === 'plan' && (
          <PlanStep 
            context={context} 
            onNext={handleNext} 
            onBack={handleBack} 
          />
        )}
        
        {currentStep === 'apply' && (
          <StatusStep 
            context={context} 
            onRestart={handleRestart} 
          />
        )}
      </main>
      
      <footer style={{ marginTop: '3rem', textAlign: 'center', fontSize: '0.875rem', color: 'var(--text-muted)' }}>
        <p>Connected to local RAIDEN service via http://127.0.0.1:8080/api</p>
      </footer>
    </>
  );
}
