import { type AppType } from "next/app";

import { api } from "~/utils/api";
import "~/styles/globals.css";

const MyApp: AppType = ({ Component, pageProps }) => {
  return (
    <main className={`p-10 font-serif`}>
      <p>Medisense AI</p>
      <Component {...pageProps} />
    </main>
  );
};

export default api.withTRPC(MyApp);
