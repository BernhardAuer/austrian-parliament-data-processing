<script>
	import LoadingSpinner from './../../../components/LoadingSpinner.svelte';

	import { Bar } from 'svelte-chartjs';
	import {
		Chart as ChartJS,
		Title,
		Tooltip,
		Legend,
		LineElement,
		CategoryScale,
		LinearScale,
		PointElement,
		BarElement
	} from 'chart.js';
	import { scrollIntoView } from 'seamless-scroll-polyfill';
	import { afterUpdate } from 'svelte';

	ChartJS.register(
		Title,
		Tooltip,
		Legend,
		LineElement,
		CategoryScale,
		LinearScale,
		PointElement,
		BarElement
	);

	export let selectedYear = null;
	export let chartDataPromise = null;
	let chart;

	const scrollToTypeOfSpeechDiagram = () => {
		scrollIntoView(document.getElementById('typeOfSpeechDiagram'), {
			behavior: 'smooth',
			block: 'start',
			inline: 'nearest'
		});
	};

	afterUpdate(() => {
		scrollToTypeOfSpeechDiagram();
	});
</script>

<h2 class="card-title">Nationalratssitzungen pro Monat in {selectedYear}</h2>
{#await chartDataPromise}
	<LoadingSpinner />
{:then chartData}
	{#if !chartData?.datasets?.length}
		<div class="flex flex-col items-center my-auto">
			<p>Für den ausgewählten Filter sind keine Daten verfügbar.</p>
		</div>
	{:else}
		<div class="relative h-[25rem]">
			<Bar
				bind:chart
				data={chartData}
				options={{
					responsive: true,
					maintainAspectRatio: false,
					scales: {
						y: {
							ticks: { precision: 0 },
							title: {
								display: true,
								text: 'Anzahl der Sitzungen'
							}
						}
					},
					plugins: {
						tooltip: {
							enabled: true,
							usePointStyle: true,
							callbacks: {
								label: (context) => {
									return context.parsed.y + " Sitzung(en)"
								}
							}
						},
						legend: {
							display: false
						}
					}
				}}
			/>
		</div>
	{/if}
{:catch error}
	Leider ist ein Fehler aufgetreten! Überprüfen Sie Ihre Internetverbindung und probieren Sie es
	später erneut.
{/await}
