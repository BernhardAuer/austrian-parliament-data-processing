<script>
	import DataFilter from './DataFilter.svelte';
	import { Doughnut } from 'svelte-chartjs';
	import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js';
	import ChartService from './../services/chartService.js';
	import LoadingSpinner from './LoadingSpinner.svelte';
	import { scrollIntoView } from "seamless-scroll-polyfill";
	import FilterOptions from './../models/filterOptions.js';
	import { onMount } from 'svelte';

	ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);
	let service = new ChartService();

	let shownFilterOptions = new FilterOptions();

	let chartData = null;
	let chart;
	
	const getHeightForDoughnut = (labelCount) => {
		if (labelCount < 5){			
			return "h-[15rem]";
		}
		if (labelCount < 10){			
			return "h-[25rem]";
		}
		if (labelCount < 15){			
			return "h-[35rem]";
		}			
		return "h-[45rem]";
		
	}	
	const scrollToTypeOfSpeechDiagram = () => {
		scrollIntoView(document.getElementById('typeOfSpeechDiagram'), { behavior: "smooth", block: "start", inline: "nearest" });
	}
	
	const populateChartData = async (event) => {
		chartData = null;		
		Object.assign(shownFilterOptions, event.detail); // shallow copy selectedFilterOptions object
		chartData = await service.fetchSpeechTypes(shownFilterOptions);
		scrollToTypeOfSpeechDiagram();
	}
	onMount(async () => {		
		shownFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];
		await populateChartData(shownFilterOptions);
	});
</script>
<div class="md:2xl:mx-96">
	<h1 class="text-4xl font-normal leading-normal mt-0 mb-2 text-blue-800 break-words">
		Übersicht aller Wortmeldungsarten im Nationalrat
	</h1>
	<p class="text-1xl  leading-tight mt-0 mb-2">
		Redebeiträge in den Plenarsitzungen des Nationalrats werden in Wortmeldungsarten kategoriersiert. Um einen Überblick über 
		die Verteilung der Wortmeldungsarten im Nationalrat zu erhalten, werden diese hier grafisch dargestellt.
		
		Benützen Sie den Filter, um die Datengrundlage nach Ihrem Interesse anzupassen.
	</p>
</div>
<div class="flex justify-center gap-x-16 gap-y-4 flex-wrap">
	<div class="card w-full sm:w-96 bg-base-100 shadow-xl">
		<div class="card-body">
			<DataFilter on:submit={populateChartData}></DataFilter>
		</div>
	</div>
	<div class="card w-full sm:w-[40rem] bg-base-100 shadow-xl" id="typeOfSpeechDiagram">
		<div class="card-body">
			
				<h2 class="card-title">Wortmeldungsarten</h2>			
				{#if chartData == null}
					<LoadingSpinner />
				{:else if !chartData.labels.length}
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
					</div>
					<div class="relative {getHeightForDoughnut(chartData?.labels?.length)}">
						<Doughnut bind:chart data={chartData} options={{responsive: true,maintainAspectRatio: false}} />
					</div>
				{/if}	
		</div>
	</div>
</div>

