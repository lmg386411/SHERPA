import React from "react";
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from "chart.js";
import { Bar } from "react-chartjs-2";

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

const options = {
  indexAxis: "y",
  elements: {
    bar: {
      borderWidth: 1,
    },
  },
  responsive: true,
  plugins: {
    legend: {
      align: "end",
    },
    title: {
      display: true,
      position: "bottom",
    },
  },
  scales: {
    x: {
      ticks: {
        callback: (value) => `${value}%`,
      },
    },
  },
};

function makeDoubleChart({ labels, firstDatas, secondDatas }) {
  const data = {
    labels,
    datasets: [
      {
        label: "2021년",
        data: firstDatas,
        borderColor: "#B4B4B4",
        backgroundColor: "#B4B4B4",
      },
      {
        label: "2022년",
        data: secondDatas,
        borderColor: "#53AC8E",
        backgroundColor: "#53AC8E",
      },
    ],
  };

  return (
    <div style={{ width: "100%" }}>
      <Bar options={options} data={data} />
    </div>
  );
}

export default makeDoubleChart;
