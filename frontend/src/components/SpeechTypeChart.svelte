<script>
	import { TypeOfSpeechCountDto } from './../javascript-client-generated/src/model/TypeOfSpeechCountDto.js';
	import { Doughnut } from 'svelte-chartjs';
	import { onMount } from 'svelte';
	import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, CategoryScale } from 'chart.js';
	import ChartService from './../services/chartService.js';
	import AutoComplete from 'simple-svelte-autocomplete';
	import LoadingSpinner from './LoadingSpinner.svelte';

	ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale);
	let service = new ChartService();

	let rerenderTrigger = 0;
	let data = null;
	let selectedTopic = null;
	let chart;
	let selectedLegislatur = null;
	let selectedMeetingNumber = null;
	let selectedPoliticalParties = ['V', 'S', 'F', 'G', 'N'];
	let legislatureAndMeetings = null;
	let currentShownMeetingNumber = null;
	let currentShownPoliticalParties = null;
	let currentShownLegislatur = null;
	let currentTopic = null;

	const resetAutoCompleter = () => {
		selectedTopic = null;
		rerenderTrigger = rerenderTrigger + 1;
	};
	$: selectedLegislatur, selectedMeetingNumber, resetAutoCompleter();
	let dataTemplate = {
		labels: [],
		datasets: [
			{
				data: [],
				backgroundColor: [],
				hoverBackgroundColor: []
			}
		]
	};
	function populateData() {
		data = null;
		service.fetchSpeechTypes(
			selectedLegislatur,
			selectedMeetingNumber,
			selectedTopic?.topNr ?? '',
			selectedPoliticalParties,
			(response) => {
				console.log(response);
				if (!Array.isArray(response) && !response.length) {
					data = dataTemplate;
					console.log("nix da.")
					return;
				}

				let typeOfSpeechCountList = Array.from(response, (element) => {
					console.log('element:' + JSON.stringify(element));
					return TypeOfSpeechCountDto.constructFromObject(element);
				});

				dataTemplate.datasets[0].data = Array.from(
					typeOfSpeechCountList,
					(element) => element.count
				);
				dataTemplate.labels = Array.from(typeOfSpeechCountList, (element) => element.typeOfSpeech);
				dataTemplate.datasets[0].backgroundColor = Array.from(typeOfSpeechCountList, (element) => mapLabelsToBackgroundColor(element.typeOfSpeech));
				dataTemplate.datasets[0].hoverBackgroundColor = Array.from(typeOfSpeechCountList, (element) => mapLabelsToHoverColor(element.typeOfSpeech));
				data = dataTemplate;
				currentShownMeetingNumber = selectedMeetingNumber;
				currentShownPoliticalParties = selectedPoliticalParties;
				currentShownLegislatur = selectedLegislatur;
				currentTopic = selectedTopic;
			}
		);
	}
	
	function mapLabelsToBackgroundColor(labelName) {
		labelName = labelName.toLowerCase();
		let colorDict = {
			"pro": "#46BFBD",
			"contra": "#F7464A",
			"erste lesung": "#949FB1",
			"regierungsbank": "#4D5360",
			"tatsächliche berichtigung": "#FDB45C",
		}
		return colorDict[labelName];
	}
	
	function mapLabelsToHoverColor(labelName) {
		labelName = labelName.toLowerCase();
		let colorDict = {
			"pro": "#5AD3D1",
			"contra": "#FF5A5E",
			"erste lesung": "#A8B3C5",
			"regierungsbank": "#616774",
			"tatsächliche berichtigung": "#FFC870",
		}
		return colorDict[labelName];
	}

	function mapPoliticalPartyAbbreviationToLongName(abbr) {
		let mapDict = {
			"v": "ÖVP",
			"s": "SPÖ",
			"f": "FPÖ",
			"g": "GRÜNE",
			"n": "NEOS"
		}
		return Array.from(abbr, (element) => {
			let abbrToLower = element.toLowerCase();
			return mapDict[abbrToLower];
		}).join(", ");
	}
	const scrollAutoCompleteToTop = () => {
		console.log("onfocus");
		document.getElementById('topNumber').scrollIntoView({behavior: "smooth", block: "start", inline: "nearest"})
	}

	onMount(async () => {
		populateData();
		legislatureAndMeetings = await service.getLegislaturesAndMeetings();
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
			<h2 class="card-title">Datenfilter</h2>	
			{#if legislatureAndMeetings == null}
					<LoadingSpinner />
			{:else}
				<div class="relative">
					<label class="block text-gray-700 text-sm font-bold mb-2 basis-2/3" for="legislatur">Gesetzgebungsperiode:</label>				
					<div class="tooltip tooltip-left absolute top-0 right-0" data-tip="Nur vollständig digitalisierte Gesetzgebungsperioden sind verfügbar.">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
							<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" />
						</svg>	
					</div>		  
					<select
						class="select select-bordered w-full  basis-1"
						bind:value={selectedLegislatur}
						name="Gesetzgebungsperiode"
						id="legislatur"
					>
						{#if legislatureAndMeetings !== null}
							{#each legislatureAndMeetings as item}
								<option value={item.legislature}>{item.legislature}</option>
							{/each}
						{/if}
					</select>
				</div>
				<div class="relative">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="meetingNumber">Sitzung:</label>
					<div class="tooltip tooltip-left absolute top-0 right-0" data-tip="Nur Sitzungen mit mind. einer kategorisierten Wortmeldungsart sind verfügbar.">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
							<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" />
						</svg>	
					</div>	
					<select
						class="select select-bordered w-full"
						bind:value={selectedMeetingNumber}
						name="Sitzung"
						id="meetingNumber"
					>
						{#if legislatureAndMeetings !== null && selectedLegislatur !== null}
							{#each legislatureAndMeetings.find(x => x.legislature === selectedLegislatur)?.meetings as meeting}
								<option value="{meeting}">{meeting}</option>
							{/each}
						{/if}
					</select>
				</div>
				<div class="testparent w-full relative">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="topNumber">TOP:</label>
					<div class="tooltip tooltip-left absolute top-0 right-0" data-tip="Die Suche nach TOPs berücksichtigt die ausgewählte Gesetzgebungsperiode und Sitzung.">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
							<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" />
						</svg>	
					</div>	
					{#key rerenderTrigger}
						<AutoComplete
							onFocus={() => scrollAutoCompleteToTop()}
							minCharactersToSearch="0"
							placeholder="Suche TOPs"
							hideArrow="true"
							inputClassName="w-full text-base"
							className="input input-bordered w-full text-base"
							noInputStyles="false"
							showClear="true"
							lock="false"
							noResultsText="Kein Suchergebnis gefunden. Geben Sie bitte vollständige Wörter ein"
							loadingText="Lade Ergebnisse..."
							searchFunction={(keyword) =>
								service.searchTopics(keyword, selectedLegislatur, selectedMeetingNumber)}
							bind:selectedItem={selectedTopic}
							labelFunction={(selected) => selected.topNr + ': ' + selected.topic}
							inputId="topNumber"
							name="TOP"
						/>
					{/key}
				</div>
				<div class="relative">
					<label class="block text-gray-700 text-sm font-bold mb-2" for="topNumber">Fraktion:</label>
					<div class="tooltip tooltip-left absolute top-0 right-0" data-tip="Vorläufig sind nur derzeit im Parlament aktive Fraktionen verfügbar.">
						<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" class="w-5 h-5">
							<path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a.75.75 0 000 1.5h.253a.25.25 0 01.244.304l-.459 2.066A1.75 1.75 0 0010.747 15H11a.75.75 0 000-1.5h-.253a.25.25 0 01-.244-.304l.459-2.066A1.75 1.75 0 009.253 9H9z" clip-rule="evenodd" />
						</svg>	
					</div>
					<div class="grid grid-cols-3 gap-2 ">
						<div class="flex flex-row gap-2 border-2 rounded-full items-center">
							<input
								type="checkbox"
								class="checkbox"
								id="politicalParty_oevp"
								bind:group={selectedPoliticalParties}
								name="ÖVP"
								value="V"
							/>
							<label for="politicalParty_oevp">ÖVP</label>
						</div>
						<div class="flex flex-row gap-2 border-2 rounded-full items-center">
							<input
								type="checkbox"
								class="checkbox"
								id="politicalParty_spoe"
								bind:group={selectedPoliticalParties}
								name="SPÖ"
								value="S"
							/>
							<label for="politicalParty_spoe">SPÖ</label>
						</div>					
						<div class="flex flex-row gap-2 border-2 rounded-full items-center">
							<input
								type="checkbox"
								class="checkbox"
								id="politicalParty_fpoe"
								bind:group={selectedPoliticalParties}
								name="FPÖ"
								value="F"
							/>
							<label for="politicalParty_fpoe">FPÖ</label>
						</div>
						<div class="flex flex-row gap-2 border-2 rounded-full items-center">
							<input
								type="checkbox"
								class="checkbox"
								id="politicalParty_gruene"
								bind:group={selectedPoliticalParties}
								name="GRÜNE"
								value="G"
							/>
							<label for="politicalParty_gruene">GRÜNE</label>
						</div>
						<div class="flex flex-row gap-2 border-2 rounded-full items-center">
							<input
								type="checkbox"
								class="checkbox"
								id="politicalParty_neos"
								bind:group={selectedPoliticalParties}
								name="NEOS"
								value="N"
							/>
							<label for="politicalParty_neos">NEOS</label>
						</div>
				</div>
					
				</div>				
				<button class="btn " on:click={() => populateData()}>Grafik aktualisieren</button>
			{/if}
		</div>
	</div>
	<div class="card w-full sm:w-96 bg-base-100 shadow-xl">
		<div class="card-body">
			
				<h2 class="card-title">Wortmeldungsarten</h2>			
				{#if data == null}
					<LoadingSpinner />
				{:else if !data.labels.length}
					<div class="flex flex-col items-center my-auto">
						<p>Für den ausgewählten Filter sind keine Daten verfügbar.</p>
					</div>
				{:else}			
					<div class="block text-gray-700 text-sm font-bold">
						{#if currentShownLegislatur != null}
							{currentShownLegislatur}. GP /
						{/if}
						{#if currentShownMeetingNumber != null}
							{currentShownMeetingNumber}. Sitzung /
						{/if}
						{#if currentTopic?.topNr != null}
							{currentTopic?.topNr} /
						{/if}
						{mapPoliticalPartyAbbreviationToLongName(currentShownPoliticalParties)}
					</div>
					<Doughnut bind:chart {data} options={{ responsive: true }} />
				{/if}	
		</div>
	</div>
</div>

<style>
	/* this is a hack ... please help me fixing */
	.testparent :global(.autocomplete) {
		padding-top: 0.7em;
	}
</style>
