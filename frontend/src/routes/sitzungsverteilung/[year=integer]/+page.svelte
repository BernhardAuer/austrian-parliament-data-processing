<script>
	import YearPicker from './../../../components/dataFilter/YearPicker.svelte';
	import NationalCouncilMeetingDistributionChart from './NationalCouncilMeetingDistributionChart.svelte';
	import ChartService from '../../../services/chartService';

	export let data;
	let chartDataPromise = data.chartData;
	let selectedYear = data.selectedYear;
	const service = new ChartService();
	const fetchChartData = async (event) => {
		selectedYear = event.detail;
		chartDataPromise = service.fetchNationalCouncilMeetingDistribution(selectedYear);
		
		// shallow routing is not possible right now
		// https://github.com/sveltejs/kit/issues/2673
		history.replaceState(history.state, document.title, `/sitzungsverteilung/${selectedYear}`);
	};
</script>

<svelte:head>
	<title>Übersicht Nationalratssitzungen | parli-info.org</title>
</svelte:head>

<div class="md:2xl:mx-96">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Übersicht abgehaltene Nationalratssitzungen
	</h1>
	<p class="text-1xl leading-tight mt-0 mb-2">
		Die Grafik visualisiert die Nationalratssitzungen pro Monat für das ausgewählte Jahr.
	</p>
</div>
<div class="flex justify-center gap-x-16 gap-y-4 flex-wrap">
	<div class="card w-full sm:w-96 bg-base-100 shadow-xl">
		<div class="card-body">
			<YearPicker
				on:submit={fetchChartData}
				selectedYear={selectedYear}
			/>
		</div>
	</div>
	<div class="card w-full sm:w-[40rem] bg-base-100 shadow-xl" id="typeOfSpeechDiagram">
		<div class="card-body">
			<NationalCouncilMeetingDistributionChart {chartDataPromise} {selectedYear} />
		</div>
	</div>
</div>
