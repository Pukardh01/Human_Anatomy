import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import questions from "../questions.json";




const Quiz = () => {
    const [currentQuestionIndex, setCurrentQuestionIndex] = useState(0);
    const [score, setScore] = useState(0);
    const [showScore, setShowScore] = useState(false);
    const [startQuiz, setStartQuiz] = useState(false);

    const navigate = useNavigate();

    const shuffledQuestions = [...questions.quiz].sort(() => 0.5 - Math.random()).slice(0, 10);

    const handleAnswerClick = (option) => {
        if (option === shuffledQuestions[currentQuestionIndex].answer) {
            setScore(score + 1);
        }

        const nextQuestion = currentQuestionIndex + 1;
        if (nextQuestion < shuffledQuestions.length) {
            setCurrentQuestionIndex(nextQuestion);
        } else {
            setShowScore(true);
        }
    };

    const handleRestart = () => {
        setScore(0);
        setCurrentQuestionIndex(0);
        setShowScore(false);
        setStartQuiz(false);
    };

    return (
        <div className="min-h-screen bg-gray-100">

<div className="flex flex-wrap px-8 py-4 bg-white justify-between items-center">
    <h5 className="text-xl font-semibold">Learn Human Anatomy</h5>
    <div className="flex items-center gap-4">
        <h5 className="text-md font-semibold">Welcome, Pukar</h5>
        <button
            className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
            onClick={() => navigate("/")}
        >
           Back to Home
        </button>
    </div>
</div>


            <div className="px-10">
                <div className="bg-white shadow-sm rounded-lg px-10 py-5">
                    {!startQuiz ? (
                        <div className="text-center">
                            <h1 className="text-2xl font-bold text-gray-800 mb-4">Welcome to the Quiz</h1>
                            <p className="text-gray-600 mb-6">Test your knowledge with this interactive quiz!</p>
                            <button
                                className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                                onClick={() => setStartQuiz(true)}
                            >
                                Start Quiz
                            </button>
                        </div>
                    ) : showScore ? (
                        <div className="text-center">
                        {/* Completion Image */}
                        <img
                            src="Animation .gif" // Replace this with the actual image URL
                            alt="Quiz Completed"
                            className="w-40 h-40 mx-auto mb-6"
                        />
                    
                        {/* Completion Message */}
                        <h2 className="text-2xl font-bold text-gray-800">Quiz Completed!</h2>
                        <p className="mt-4 text-lg text-gray-600">
                            Your score: <span className="text-blue-500">{score}</span> out of{" "}
                            <span className="text-blue-500">{shuffledQuestions.length}</span>
                        </p>
                    
                        {/* Restart Quiz Button */}
                        <button
                            className="mt-6 px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600 mb-3"
                            onClick={handleRestart}
                        >
                            Restart Quiz
                        </button>
                        <br />
                    
                        {/* Back to Home Button */}
                        <button
                            className="px-4 py-2 bg-blue-500 text-white rounded-md hover:bg-blue-600"
                            onClick={() => navigate("/")}
                        >
                            Back to Home
                        </button>
                    </div>
                    
                    ) : (
                        <div>
                            <div className="text-xl font-semibold text-gray-800 mb-4">
                                Question {currentQuestionIndex + 1} / {shuffledQuestions.length}
                            </div>
                            <p className="text-gray-700 mb-6">{shuffledQuestions[currentQuestionIndex].question}</p>
                            <div className="grid gap-4">
                                {Object.entries(shuffledQuestions[currentQuestionIndex].options).map(([key, value]) => (
                                    <button
                                        key={key}
                                        className="px-4 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-blue-500 hover:text-white transition"
                                        onClick={() => handleAnswerClick(parseInt(key))}
                                    >
                                        {value}
                                    </button>
                                ))}
                            </div>
                        </div>
                    )}

                </div>
            </div>


        </div>
    );
};

export default Quiz;
