import React from 'react';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js';
import { Line } from 'react-chartjs-2';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

export function makeLineChart({ labels, weekdaysDatas, weekendsDatas, text }) {
  const options = {
    responsive: true,
    plugins: {
      legend: {
        align: 'end'
      },
      title: {
        display: true,
        text: text,
        position: 'bottom',
        color: '#959191',
        font: {
          size: 16
        }
      }
    },
    scales: {
      y: {
        ticks: {
          callback: function (value) {
            return value + '%'; // y축 값에 백분율(%) 추가
          }
        }
      }
    }
  };

  const data = {
    labels,
    datasets: [
      {
        label: '주말 이용률',
        data: weekdaysDatas,
        borderColor: '#53AC8E',
        backgroundColor: '#53AC8E'
      },
      {
        label: '주중 이용률',
        data: weekendsDatas,
        borderColor: '#F8CE7E',
        backgroundColor: '#F8CE7E'
      }
    ]
  };

  return (
    <div style={{ width: '100%' }}>
      <Line options={options} data={data} />
    </div>
  );
}

export default makeLineChart;
