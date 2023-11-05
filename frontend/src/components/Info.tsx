import Image from "next/image";
import Link from "next/link";
import graph from "~/images/graph.png";


export default function Info() {
    return (
      <div id="info" className="bg-white py-24 sm:py-32">
        <div className="mx-auto max-w-7xl px-6 lg:px-8">
          <div className="mx-auto max-w-2xl lg:mx-0 lg:max-w-none">
            <p className="text-base font-semibold leading-7 text-indigo-600">Prevent errors</p>
            <h1 className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">Safer patient experience</h1>
            <div className="mt-10 grid max-w-xl grid-cols-1 gap-8 text-base leading-7 text-gray-700 lg:max-w-none lg:grid-cols-2">
              <div>
                <p>
                  Using a model we trained on pre existing medical data, a doctor can input a patient&apos;s FHIR file and a disease they are testing for,
                  and our model will determine if the patient is at risk for the specificied disease.
                </p>
               
              </div>
              <div>
                <p>
                  Our model will then reveal a kernel density estimate plot to show how the output was determined.
                </p>
               
              </div>
            </div>
            <div className="mt-10 flex">
              <Link
                href="/predict"
                className="rounded-md bg-indigo-600 px-3.5 py-2.5 text-sm font-semibold text-white shadow-sm hover:bg-indigo-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                Start predicting
              </Link>
            </div>
          </div>
        </div>
        <div className="relative overflow-hidden pt-16 lg:pt-20">
          <div className="mx-auto max-w-7xl px-6 lg:px-8">
            <Image
              className="mb-[-12%] rounded-xl shadow-2xl ring-1 ring-gray-900/10"
              src={graph}
              alt="graph of sample user data"
            />
            <div className="relative" aria-hidden="true">
              <div className="absolute -inset-x-20 bottom-0 bg-gradient-to-t from-white pt-[7%]" />
            </div>
          </div>
        </div>
      </div>
    )
  }
  