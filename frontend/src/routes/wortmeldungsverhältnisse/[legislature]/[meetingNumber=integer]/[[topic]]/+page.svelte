<script>
	import DataFilter from '../../../../../components/dataFilter/DataFilter.svelte';
	import ChartService from '../../../../../services/chartService';
	import FilterOptions from '../../../../../models/filterOptions';
	import SpeechDistributionChart from '../../../../../components/SpeechDistributionChart.svelte';

	export let data;
	let chartDataPromise = data.chartData;
	let shownFilterOptions = new FilterOptions(structuredClone(data.selectedFilterOptions));
	const service = new ChartService();
	const fetchChartData = async (event) => {
		shownFilterOptions = new FilterOptions(structuredClone(event.detail));
		chartDataPromise = service.fetchDistributionOfSpeakingTime(shownFilterOptions);

		const topicEncoded = encodeURIComponent(shownFilterOptions?.topic?.topic) ?? '';
		// shallow routing is not possible right now
		// https://github.com/sveltejs/kit/issues/2673
		history.replaceState(
			history.state,
			document.title,
			`/wortmeldungsverhältnisse/${shownFilterOptions.legislature}/${shownFilterOptions.meetingNumber}/${topicEncoded}?fraktion=${shownFilterOptions.politicalParties}`
		);
	};
</script>

<svelte:head>
	<title>Wortmeldungsverhältnis | parli-info.org</title>
</svelte:head>

<div class="md:2xl:mx-96">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Übersicht über das Verhältnis von Anzahl und Dauer der Wortmeldungen im Nationalrat
	</h1>
	<p class="text-1xl leading-tight mt-0 mb-2">
		Die Grafik visualisiert das Verhältnis von Sprechdauer bzw. Anzahl an Wortmeldungen pro Fraktion
		im Nationalrat.
	</p>
</div>
<div class="flex justify-center gap-x-16 gap-y-4 flex-wrap">
	<div class="card w-full sm:w-96 bg-base-100 shadow-xl">
		<div class="card-body">
			<DataFilter
				on:submit={fetchChartData}
				legislatureAndMeetings={data.legislatureAndMeetings}
				selectedFilterOptions={data.selectedFilterOptions}
			/>
		</div>
	</div>
	<div class="card w-full sm:w-[40rem] bg-base-100 shadow-xl" id="typeOfSpeechDiagram">
		<div class="card-body">
			<div class="tooltip tooltip-left absolute top-10 right-7" data-tip="Durch einen Klick auf die Texte 'Sprechdauer' bzw. 'Anzahl Wortmeldungen' können die jeweiligen Balken in der Grafik ausgeblendet werden.">
				<svg
					xmlns="http://www.w3.org/2000/svg"
					viewBox="0 0 20 20"
					fill="currentColor"
					class="w-5 h-5"
				>
					<path
						fill-rule="evenodd"
						d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z"
						clip-rule="evenodd"
					/>
				</svg>
			</div>
			<SpeechDistributionChart {chartDataPromise} {shownFilterOptions} />
		</div>
	</div>
</div>
