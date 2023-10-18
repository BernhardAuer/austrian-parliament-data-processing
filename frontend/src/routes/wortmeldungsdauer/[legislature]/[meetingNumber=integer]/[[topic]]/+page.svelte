<svelte:head>
	<title>Wortmeldungsdauer | parli-info.org</title>
</svelte:head>

<script>
	import DataFilter from './../../../../../components/dataFilter/DataFilter.svelte';
	import ChartService from './../../../../../services/chartService';
	import FilterOptions from './../../../../../models/filterOptions';
	import SpeechDurationChart from '../../../../../components/SpeechDurationChart.svelte';

    export let data;
	let chartDataPromise = data.chartData;
	let shownFilterOptions = new FilterOptions(structuredClone(data.selectedFilterOptions));
	const service = new ChartService;
	const fetchChartData = async (event) => {
		shownFilterOptions = new FilterOptions(structuredClone(event.detail));
		chartDataPromise = service.fetchSpeechDurations(shownFilterOptions);

		const topicEncoded = shownFilterOptions?.topic?.topic?.replace('/', '%2F') ?? '';
		// shallow routing is not possible right now
		// https://github.com/sveltejs/kit/issues/2673
		history.replaceState(history.state, document.title, `/wortmeldungsdauer/${shownFilterOptions.legislature}/${shownFilterOptions.meetingNumber}/${topicEncoded}?fraktion=${shownFilterOptions.politicalParties}`)
	}

</script>

<div class="md:2xl:mx-96">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Übersicht über Anzahl und Dauer der Wortmeldungen im Nationalrat
	</h1>
	<p class="text-1xl leading-tight mt-0 mb-2">
		In dieser Grafik werden die Redebeiträge der Parlamentarier:innen im Nationalrat nach Häufigkeit und Dauer dargestellt.
	</p>
</div>
<div class="flex justify-center gap-x-16 gap-y-4 flex-wrap">
	<div class="card w-full sm:w-96 bg-base-100 shadow-xl">
		<div class="card-body">
			<DataFilter on:submit={fetchChartData} legislatureAndMeetings={data.legislatureAndMeetings} selectedFilterOptions={data.selectedFilterOptions}/>
		</div>
	</div>
	<div class="card w-full sm:w-[40rem] bg-base-100 shadow-xl" id="typeOfSpeechDiagram">
		<div class="card-body">
			<SpeechDurationChart {chartDataPromise} {shownFilterOptions}/>
		</div>
	</div>
</div>
