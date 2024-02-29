import React, { useRef, useEffect } from 'react';
import { Chart, RadialLinearScale } from 'chart.js';
import { WordCloudController, WordElement } from 'chartjs-chart-wordcloud';
import styled from 'styled-components';

Chart.register(WordCloudController, WordElement, RadialLinearScale);

const StyledCanvas = styled.canvas`
  display: block;
  width: 600px;
  height: 400px;
  border: 1px #b5b5b5 solid;
`;

const WordCloud = ({ data, onWordClick }) => {
  const canvasRef = useRef(null);
  const chartInstance = useRef(null);

  const desiredWidth = 500;
  const desiredHeight = 500;

  const MIN_FONT_SIZE = 10; // 원하는 최소 폰트 크기를 설정
  const MAX_FONT_SIZE = 40; // 원하는 최대 폰트 크기를 설정

  // 색상 배열
  const colors = [
    'red',
    'blue',
    '#FF33FF',
    '#FFFF99',
    '#00B3E6',
    '#E6B333',
    '#3366E6',
    '#999966',
    '#99E6E6',
    '#66664D'
  ];

  useEffect(() => {
    const canvas = canvasRef.current;
    canvas.width = desiredWidth;
    canvas.height = desiredHeight;

    // console.log('좀 나와주면 안될까?', data.datasets[0].data);
    // 데이터 검증: data.datasets[0].data가 배열인지 확인
    if (!Array.isArray(data.datasets[0].data)) {
      console.error('Data is not an array:', data.datasets[0].data);
      return; // early return to prevent further execution
    }

    // 데이터 전처리: 각 데이터 포인트를 조건적으로 조정합니다.
    const adjustedData = data.datasets[0].data.map((point) =>
      point < MIN_FONT_SIZE ? MIN_FONT_SIZE : point > MAX_FONT_SIZE ? MAX_FONT_SIZE : point
    );

    // 각 단어에 랜덤 색상 할당
    data.labels.forEach((label, index) => {
      data.datasets[0].backgroundColor = data.datasets[0].backgroundColor || [];
      data.datasets[0].backgroundColor[index] = colors[Math.floor(Math.random() * colors.length)];
    });
    // console.log('워드컬러', data.datasets[0].backgroundColor);
    // console.log('워드컬러', typeof data.datasets[0].backgroundColor[0]);

    const options = {
      responsive: false,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false
        }
      }
    };

    // 원본 데이터의 복사본을 만들고, 조정된 데이터로 갱신
    const newData = {
      ...data,
      datasets: [
        {
          ...data.datasets[0],
          data: adjustedData,
          backgroundColor: data.datasets[0].backgroundColor // Use the colors in the data
        }
      ]
    };

    chartInstance.current = new Chart(canvas, {
      type: 'wordCloud',
      data: newData,
      options
    });

    const handleClick = (event) => {
      const elements = chartInstance.current.getElementsAtEventForMode(event, 'nearest', { intersect: true }, false);

      if (elements.length > 0) {
        const element = elements[0];
        console.log('선택한 단어', chartInstance.current.data.labels[element.index]);
        const word = chartInstance.current.data.labels[element.index];
        onWordClick(word);
      }
    };

    // Add the click event listener to the canvas
    canvasRef.current.addEventListener('click', handleClick);

    // Cleanup: remove the event listener when the component is unmounted
    return () => {
      // 이벤트 리스너 정리
      if (canvasRef.current) {
        canvasRef.current.removeEventListener('click', handleClick);
      }

      // 차트 인스턴스 정리
      chartInstance.current && chartInstance.current.destroy();
    };
  }, [data, onWordClick]);

  return <StyledCanvas ref={canvasRef} />;
};

export default WordCloud;
