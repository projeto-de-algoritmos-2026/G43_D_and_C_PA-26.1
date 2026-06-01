const elements = {
  p50: document.querySelector("#p50"),
  average: document.querySelector("#average"),
  count: document.querySelector("#count"),
  max: document.querySelector("#max"),
  range: document.querySelector("#range"),
  chart: document.querySelector("#chart"),
  simulateSmall: document.querySelector("#simulate-small"),
  simulateLarge: document.querySelector("#simulate-large"),
  reset: document.querySelector("#reset"),
};

function formatMs(value) {
  return value === null || value === undefined ? "--" : `${Number(value).toFixed(2)} ms`;
}

function updateCards(data) {
  elements.p50.textContent = formatMs(data.p50_ms);
  elements.average.textContent = formatMs(data.average_ms);
  elements.count.textContent = data.count ?? 0;
  elements.max.textContent = formatMs(data.max_ms);
  elements.range.textContent = data.min_ms === null
    ? "Sem dados ainda"
    : `Min ${formatMs(data.min_ms)} | Max ${formatMs(data.max_ms)}`;
}

function drawChart(values) {
  const canvas = elements.chart;
  const context = canvas.getContext("2d");
  const width = canvas.width;
  const height = canvas.height;
  const padding = 28;

  context.clearRect(0, 0, width, height);
  context.fillStyle = "#ffffff";
  context.fillRect(0, 0, width, height);

  if (!values || values.length === 0) {
    context.fillStyle = "#607089";
    context.font = "18px Arial";
    context.fillText("Clique em simular para gerar latencias.", padding, height / 2);
    return;
  }

  const max = Math.max(...values);
  const min = Math.min(...values);
  const span = Math.max(1, max - min);
  const step = (width - padding * 2) / Math.max(1, values.length - 1);

  context.strokeStyle = "#dfe5ee";
  context.lineWidth = 1;
  for (let index = 0; index < 5; index += 1) {
    const y = padding + ((height - padding * 2) / 4) * index;
    context.beginPath();
    context.moveTo(padding, y);
    context.lineTo(width - padding, y);
    context.stroke();
  }

  context.strokeStyle = "#1f6feb";
  context.lineWidth = 3;
  context.beginPath();
  values.forEach((value, index) => {
    const x = padding + index * step;
    const y = height - padding - ((value - min) / span) * (height - padding * 2);
    if (index === 0) {
      context.moveTo(x, y);
    } else {
      context.lineTo(x, y);
    }
  });
  context.stroke();
}

async function fetchMetrics() {
  const response = await fetch("/api/metrics");
  const data = await response.json();
  updateCards(data);
  drawChart(data.recent_ms);
}

async function simulate(count) {
  const response = await fetch(`/api/simulate?count=${count}`, { method: "POST" });
  const data = await response.json();
  updateCards(data);
  drawChart(data.recent_ms);
}

async function resetMetrics() {
  const response = await fetch("/api/reset", { method: "POST" });
  const data = await response.json();
  updateCards(data);
  drawChart([]);
}

elements.simulateSmall.addEventListener("click", () => simulate(1000));
elements.simulateLarge.addEventListener("click", () => simulate(10000));
elements.reset.addEventListener("click", resetMetrics);

fetchMetrics();
setInterval(fetchMetrics, 5000);
