import { Link } from "react-router-dom";

export function LandingPage() {
  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-50 via-white to-sky-100 px-6 py-14">
      <section className="mx-auto max-w-4xl rounded-2xl border border-slate-200 bg-white/80 p-8 shadow-xl backdrop-blur">
        <p className="mb-3 inline-flex rounded-full bg-slate-900 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-white">
          Universal Events
        </p>
        <h1 className="text-4xl font-bold tracking-tight text-slate-900 sm:text-5xl">
          Group Ticket Booking Platform
        </h1>
        <p className="mt-4 max-w-2xl text-base text-slate-600 sm:text-lg">
          Start a group registration as a public user, or sign in to the admin
          panel to manage bookings.
        </p>
        <div className="mt-8 flex flex-wrap gap-3">
          <Link
            to="/register"
            className="rounded-lg bg-slate-900 px-5 py-2.5 text-sm font-semibold text-white transition hover:bg-slate-700"
          >
            Go to Registration
          </Link>
          <Link
            to="/admin/login"
            className="rounded-lg border border-slate-300 bg-white px-5 py-2.5 text-sm font-semibold text-slate-700 transition hover:border-slate-400 hover:bg-slate-100"
          >
            Admin Login
          </Link>
          <Link
            to="/admin/dashboard"
            className="rounded-lg border border-slate-300 bg-white px-5 py-2.5 text-sm font-semibold text-slate-700 transition hover:border-slate-400 hover:bg-slate-100"
          >
            Admin Dashboard
          </Link>
        </div>
      </section>
      <div className="mx-auto mt-8 max-w-4xl rounded-xl border border-sky-200 bg-sky-50 p-5 text-sm text-sky-900">
        Tailwind is installed and active. Next step is implementing the full
        registration/payment/admin workflows.
      </div>
    </main>
  );
}
