<script>
	import { Scatter } from 'svelte-chartjs';
	import { Chart as ChartJS, Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement, LogarithmicScale } from 'chart.js';
	import LoadingSpinner from './LoadingSpinner.svelte';
	import { scrollIntoView } from 'seamless-scroll-polyfill';
	import { afterUpdate } from 'svelte';

	ChartJS.register(Title, Tooltip, Legend, LineElement, CategoryScale, LinearScale, PointElement);

	export let shownFilterOptions = null;
	export let chartDataPromise = null;
	let chart;

	const getHeightForDoughnut = (labelCount) => {
		if (labelCount < 10) {
			return 'h-[25rem]';
		}
		if (labelCount < 15) {
			return 'h-[35rem]';
		}
		return 'h-[45rem]';
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

<h2 class="card-title">Wortmeldungsarten</h2>
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
		<div class="relative {getHeightForDoughnut(chartData?.labels?.length)}">
			<Scatter bind:chart data={chartData} options={{ responsive: true, maintainAspectRatio: false, parsing: { xAxisKey: "durationSumInSec", yAxisKey: "totalNumberOfSpeeches"}}} />
		</div>
	{/if}
{:catch error}
	Leider ist ein Fehler aufgetreten! Überprüfen Sie Ihre Internetverbindung und probieren Sie es
	später erneut.
{/await}
