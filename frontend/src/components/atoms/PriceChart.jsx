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

const colors = [
  "#D33B4D",
  "#F8CE7E",
  "#B4B4B4",
  "#53AC8E",
  "#383D49",
  "#E2816B",
  "#2196F3",
  "#0B0B0B",
];

function makeSingleChart({ labels, datas, text, width }) {
  const backgroundColors = colors.slice(0, datas.length);
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
        display: false,
      },
      title: {
        display: true,
        text: text,
        align: "end",
        color: "#959191",
        font: {
          size: 16,
        },
      },
    },
    scales: {
      x: {
        // max: 100,
        ticks: {
          callback: (value) => `${value}만원`,
        },
      },
    },
  };
  const data = {
    labels,
    datasets: [
      {
        label: "2021년",
        data: datas,
        borderColor: backgroundColors,
        backgroundColor: backgroundColors,
      },
    ],
  };

  return (
    <div style={{ width: width }}>
      <Bar options={options} data={data} />
    </div>
  );
}

export default makeSingleChart;
