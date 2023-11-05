import { type AppType } from "next/app";

import { api } from "~/utils/api";
import "~/styles/globals.css";
import Navbar from "~/components/Navbar";
import Head from "next/head";

const MyApp: AppType = ({ Component, pageProps }) => {
  return (
    <main className={` font-serif`}>
      <Head>
        <title>
          Medisense
        </title>
        <link rel="icon" href="/logo.png" />

      </Head>
      <Navbar />
      <Component {...pageProps} />
    </main>
  );
};

export default api.withTRPC(MyApp);
