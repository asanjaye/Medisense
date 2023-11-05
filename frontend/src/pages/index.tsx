import Head from "next/head";
import Link from "next/link";
import { useRef, useState } from "react";
import Combo from "~/components/Combobox";


import { api } from "~/utils/api";

export default function Home() {
  const hello = api.post.hello.useQuery({ text: "from tRPC" });

  const [selectedPerson, setSelectedPerson] = useState<string>("");

  const fileInputRef = useRef<HTMLInputElement | null>(null);
  const [file, setFile] = useState<File>();

  const clearFileInput = () => {
    if (fileInputRef.current) {
      fileInputRef.current.value = "";
      setFile(undefined);
    }
  };

  const runAPI = () => {};

  return (
    <main >
      <div className="flex min-h-full md:w-3/5 lg:w-1/2 mx-auto py-20 flex-col items-center justify-center gap-5">
        <p>Welcome to medisense!</p>

        <Combo
          setSelectedPerson={setSelectedPerson}
          selectedPerson={selectedPerson}
        />

        <div className="flex text-md w-full flex-col gap-2">
          <p>Upload JSON or XML file here!</p>
          <input
            className="w-full cursor-pointer rounded-md border-0 bg-white py-1.5 pl-3 pr-10 text-gray-900 shadow-sm ring-1 ring-inset ring-gray-300 focus:ring-2 focus:ring-inset focus:ring-indigo-600 sm:text-sm sm:leading-6"
            onChange={(e) => setFile(e.target.files![0])}
            accept=".xml,.json"
            ref={fileInputRef}
            type="file"
          />

        </div>
        <div className="mx-auto w-full flex flex-col gap-3">
          {file && (
            <button
              className="rounded-md bg-red-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-red-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-red-600"
              onClick={clearFileInput}
            >
              Clear file
            </button>
          )}

          <button
            className="rounded-md bg-indigo-600 px-3 py-2 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
            onClick={runAPI}
          >
            Submit
          </button>
        </div>
      </div>
    </main>
  );
}
