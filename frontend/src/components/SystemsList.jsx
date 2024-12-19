import React, { useState, useEffect } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";

const SystemsList = () => {
    const [systems, setSystems] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [selectedSystem, setSelectedSystem] = useState(null);
    const [modalData, setModalData] = useState(null); // State for modal data

    const navigate = useNavigate();

    useEffect(() => {
        const fetchSystems = async () => {
            try {
                const response = await axios.get("http://127.0.0.1:8000/systems");
                setSystems(response.data.systems);
                setLoading(false);
            } catch (err) {
                setError("Failed to fetch systems data.");
                setLoading(false);
            }
        };

        fetchSystems();
    }, []);

    const fetchSystemDetails = async (systemName) => {
        try {
            const response = await axios.get(
                `http://127.0.0.1:8000/system/${encodeURIComponent(systemName)}`
            );
            setSelectedSystem(response.data);
        } catch (err) {
            alert("Failed to fetch system details.");
        }
    };

    const handleLearnMore = (organ) => {
        setModalData(organ);
    };

    const closeModal = () => {
        setModalData(null);
    };

    if (loading) {
        return <div className="text-center text-gray-600">Loading...</div>;
    }

    if (error) {
        return <div className="text-center text-red-600">{error}</div>;
    }

    return (
        <div className="min-h-screen bg-gray-100">
            <div className="flex flex-wrap px-8 py-4 bg-white justify-between items-center">
                <h5 className="text-xl font-semibold">Learn Human Anatomy</h5>
                <div className="flex items-center gap-4">
                    <h5 className="text-md font-semibold">Welcome, Pukar</h5>
                    <button
                        className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                        onClick={() => navigate("/quiz")}
                    >
                        Start Quiz
                    </button>
                </div>
            </div>

            <div className="flex flex-row gap-4 px-10 py-5">
                <div className="w-1/2">
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
                        {systems.map((system, index) => (
                            <div
                                key={index}
                                onClick={() => fetchSystemDetails(system.name)}
                                className="bg-white shadow-sm rounded-md p-4 hover:shadow-lg transition-shadow cursor-pointer"
                            >
                                {system.image_url !== "None" && system.image_url !== null ? (
                                    <img
                                        src={system.image_url}
                                        alt={system.name}
                                        className="w-full h-48 object-contain rounded-md"
                                    />
                                ) : (
                                    <div className="w-full h-48 bg-gray-200 rounded-md flex items-center justify-center text-gray-500">
                                        No Image Available
                                    </div>
                                )}
                                <h2 className="text-md text-center font-semibold text-blue-600">
                                    {system.name}
                                </h2>
                            </div>
                        ))}
                    </div>
                </div>

                <div className="w-1/2">
                    {selectedSystem ? (
                        <div className="p-4 bg-white shadow-sm rounded">
                            <div className="flex flex-row gap-5">
                                <div className="w-1/3">
                                    {selectedSystem.image_url ? (
                                        <img
                                            src={selectedSystem.image_url}
                                            alt={selectedSystem.name}
                                            className="w-full h-full object-contain rounded-md mb-4"
                                        />
                                    ) : (
                                        <div className="w-full h-48 bg-gray-200 rounded-md flex items-center justify-center text-gray-500 mb-4">
                                            No Image
                                        </div>
                                    )}
                                </div>
                                <div className="w-2/3">
                                    <h2 className="text-xl font-bold text-blue-600 mb-2">
                                        {selectedSystem.name}
                                    </h2>
                                    <p className="text-gray-600 text-justify">{selectedSystem.description}</p>
                                </div>
                            </div>

                            <h3 className="text-xl font-semibold text-gray-800 mb-3">Organs:</h3>
                            {selectedSystem.organs.length > 0 ? (
                            <div className="flex flex-nowrap gap-4 overflow-x-auto justify-between">
                            {selectedSystem.organs.map((organ, organIndex) => (
                                <div
                                    key={organIndex}
                                    className="flex flex-col items-center border rounded-lg p-2 hover:shadow-sm transition-shadow cursor-pointer flex-shrink-0 w-48"
                                >
                                    {organ.image_url ? (
                                        <img
                                            src={organ.image_url}
                                            alt={organ.name}
                                            className="w-full h-40 object-contain rounded-md mb-2"
                                        />
                                    ) : (
                                        <div className="w-full h-40 bg-gray-200 rounded-md flex items-center justify-center text-gray-500 mb-2">
                                            No Image
                                        </div>
                                    )}
                                    <h2 className="text-md font-semibold text-blue-600 text-center mb-2">
                                        {organ.name}
                                    </h2>
                                    <p className="text-gray-500 text-justify mb-2">
                                        {organ.main_function.split(" ").slice(0, 10).join(" ")}...
                                    </p>
                                    <button
                                        className="px-3 py-1 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                                        onClick={() => handleLearnMore(organ)}
                                    >
                                        View Details
                                    </button>
                                </div>
                            ))}
                        </div>
                        
                            ) : (
                                <p className="text-gray-600">No organs listed.</p>
                            )}
                        </div>
                    ) : (
                        <div className="p-6 h-[650px] bg-white shadow-sm rounded-lg">
                            <img src="undraw_online-learning_tgmv.png" alt="hero-img"></img>
                        </div>
                    )}
                </div>
            </div>

            {modalData && (
              <div className="fixed inset-0 bg-gray-800 bg-opacity-50 flex items-center justify-center z-50">
              <div className="bg-white rounded-lg p-6 max-w-lg w-full shadow-lg">
                  {/* Heading for Organ Details */}
                  <h1 className="text-xl font-bold text-gray-800 mb-4">Organ Details</h1>
          
                  <div className="flex justify-end">
                      <button
                          className="text-gray-600 hover:text-gray-800 font-bold text-lg"
                          onClick={closeModal}
                      >
                          &times;
                      </button>
                  </div>
                  {modalData.image_url ? (
                      <img
                          src={modalData.image_url}
                          alt={modalData.name}
                          className="w-full h-48 object-contain rounded-md mb-4"
                      />
                  ) : (
                      <div className="w-full h-48 bg-gray-200 rounded-md flex items-center justify-center text-gray-500 mb-4">
                          No Image
                      </div>
                  )}
                  <h2 className="text-lg font-semibold text-blue-600 mb-4">{modalData.name}</h2>
                  <p className="text-gray-600">{modalData.main_function}</p>
                  <button
                      className="mt-4 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                      onClick={closeModal}
                  >
                      Close
                  </button>
              </div>
          </div>
          
            )}
        </div>
    );
};

export default SystemsList;
