import { FaRecycle } from 'react-icons/fa';

export default function Header() {
  return (
    <header className="header">
      <div className="header-left">
        <div className="header-logo">
          <FaRecycle />
        </div>
        <div>
          <div className="header-title">CivicLoop AI</div>
          <div className="header-subtitle">Predictive Waste Intelligence &amp; Verified Civic Action Network</div>
        </div>
      </div>
      <div className="header-right">
        <div className="header-badge">
          <span className="pulse-dot"></span>
          System Online
        </div>
        <div className="header-team">⚡ Algorithmic Thunder Squad</div>
      </div>
    </header>
  );
}
