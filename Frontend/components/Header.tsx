import Link from 'next/link';

export default function Header() {
  return (
    <header className="container">
      <nav>
        <ul>
          <li><strong>My Consulting Site</strong></li>
        </ul>
        <ul>
          <li><Link href="/">Home</Link></li>
          <li><a href="/about">About</a></li>
          <li><a href="/services">Services</a></li>
          <li><a href="/booking">Booking</a></li>
          <li><a href="/contact">Contact</a></li>
        </ul>
      </nav>
    </header>
  );
}