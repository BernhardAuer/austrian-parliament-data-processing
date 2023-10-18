<script>
	import { Scatter } from 'svelte-chartjs';
	import {
		Chart as ChartJS,
		Title,
		Tooltip,
		Legend,
		LineElement,
		CategoryScale,
		LinearScale,
		PointElement,
		LogarithmicScale
	} from 'chart.js';
	import LoadingSpinner from './LoadingSpinner.svelte';
	import { scrollIntoView } from 'seamless-scroll-polyfill';
	import { afterUpdate } from 'svelte';

	ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

	export let shownFilterOptions = null;
	export let chartDataPromise = null;
	let chart;

	const convertLengthToReadableString = (lengthInSec) => {
		const zeroPad = (num, places) => String(num).padStart(places, '0');
		let sec = zeroPad(lengthInSec % 60, 2);
		let min = Math.trunc(lengthInSec / 60);

		if (sec == 0) {
			return `${min}`;
		} else {
			return `${min}:${sec}`;
		}
	};

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

<h2 class="card-title">Wortmeldungsdauer</h2>
{#await chartDataPromise}
	<LoadingSpinner />
{:then chartData}
	{#if !chartData?.datasets?.length}
		<div class="flex flex-col items-center my-auto">
			<p>Für den ausgewählten Filter sind keine Daten verfügbar.</p>
		</div>
	{:else}
		<div class="block text-gray-700 text-sm font-bold">
			{#if shownFilterOptions.legislature != null}
				{shownFilterOptions.legislature}. GP /
			{/if}
			{#if shownFilterOptions.meetingNumber != null}
				{shownFilterOptions.meetingNumber}. Sitzung /
			{/if}
			{#if shownFilterOptions.topic?.topNr != null}
				{shownFilterOptions.topic?.topNr} /
			{/if}
			{shownFilterOptions.longNamesOfPoliticalParties}
			<br />
			{#if shownFilterOptions.legislature != null && shownFilterOptions.meetingNumber != null}
				<a
					class="link"
					href="/wortmeldungen/{shownFilterOptions.legislature}/{shownFilterOptions.meetingNumber}"
					>Zu den Wortmeldungen</a
				>
			{/if}
		</div>
		<div class="relative h-[25rem]">
			<Scatter
				bind:chart
				data={chartData}
				options={{
					responsive: true,
					maintainAspectRatio: false,
					parsing: { xAxisKey: 'durationSumInMin', yAxisKey: 'totalNumberOfSpeeches' },
					scales: {
						y: {
							beginAtZero: true,
							ticks: { precision: 0 },
							title: {
								display: true,
								text: 'Anzahl der Reden'
							}
						},
						x: {
							title: {
								display: true,
								text: 'Dauer der Reden [min]'
							}
						}
					},
					plugins: {
						tooltip: {
							enabled: true,
							usePointStyle: true,
							callbacks: {
								title: (context) => {
									return context[0].parsed.y + " Wortmeldung(en)";
								},
								label: (context) => {
									console.log(JSON.stringify(context.dataset.data[context.dataIndex]))
									return context.dataset.data[context.dataIndex].speaker + " " + convertLengthToReadableString(context.dataset.data[context.dataIndex].durationSumInSec) + " min"
								}
							}
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
