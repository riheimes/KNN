import Image from 'next/image';
import Link from 'next/link';
import './Header.css';

export default function Header() {
  return (
    <header className="header">
      <div className="header-logo">
        <Link href="/">
          <Image src="/signature_logo.png.jpg" alt="Signature Logo" width={160} height={60} />
        </Link>
      </div>

      <div className="header-slogan">
        Training as unique as your signature
      </div>

      <nav className="header-nav">
        <ul>
          <li><Link href="/">Home</Link></li>
          <li><Link href="/about">About</Link></li>
          <li><Link href="/services">Services</Link></li>
          <li><Link href="/booking">Booking</Link></li>
          <li><Link href="/contact">Contact</Link></li>
        </ul>
      </nav>
    </header>
  );
}
