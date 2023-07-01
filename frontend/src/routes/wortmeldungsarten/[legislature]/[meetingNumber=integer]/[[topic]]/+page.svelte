<svelte:head>
	<title>Wortmeldungsarten | parli-info.org</title>
</svelte:head>

<script>
	import DataFilter from './../../../../../components/dataFilter/DataFilter.svelte';
	import SpeechTypeChart from './../../../../../components/SpeechTypeChart.svelte';	
	import ChartService from './../../../../../services/chartService';
	import FilterOptions from './../../../../../models/filterOptions';

    export let data;
	let chartData = data.chartData;
	let shownFilterOptions = new FilterOptions(structuredClone(data.selectedFilterOptions));
	const service = new ChartService;
	const fetchChartData = async (event) => {
		chartData = null;
		shownFilterOptions = new FilterOptions(structuredClone(event.detail));
		chartData = await service.fetchSpeechTypes(shownFilterOptions);

		const topicEncoded = shownFilterOptions?.topic?.topic?.replace('/', '%2F') ?? '';
		// shallow routing is not possible right now
		// https://github.com/sveltejs/kit/issues/2673
		history.replaceState(history.state, document.title, `/wortmeldungsarten/${shownFilterOptions.legislature}/${shownFilterOptions.meetingNumber}/${topicEncoded}`)
	}

</script>

<div class="md:2xl:mx-96">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Übersicht aller Wortmeldungsarten im Nationalrat
	</h1>
	<p class="text-1xl leading-tight mt-0 mb-2">
		Redebeiträge in den Plenarsitzungen des Nationalrats werden in Wortmeldungsarten
		kategoriersiert. Um einen Überblick über die Verteilung der Wortmeldungsarten im Nationalrat zu
		erhalten, werden diese hier grafisch dargestellt. Benützen Sie den Filter, um die Datengrundlage
		nach Ihrem Interesse anzupassen.
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
			<SpeechTypeChart chartData={chartData} shownFilterOptions={shownFilterOptions}/>
		</div>
	</div>
</div>
