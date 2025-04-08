export default function ContactPage() {
  return (
    <main className="container">
      <h1>Contact Us</h1>
      <p>We&apos;d love to hear from you. Send us a message anytime.</p>

      <form>
        <label>
          Name
          <input type="text" required />
        </label>

        <label>
          Email
          <input type="email" required />
        </label>

        <label>
          Message
          <textarea rows={5} required />
        </label>

        <button type="submit">Send</button>
      </form>
    </main>
  );
}