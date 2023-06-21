<script>
	import { onMount } from 'svelte';
	import ChartService from './../../services/chartService';
	import LoadingSpinner from './../LoadingSpinner.svelte';
	import FilterOptions from './../../models/filterOptions';
	import { createEventDispatcher } from 'svelte';
	import DataFilterSelect from './DataFilterSelect.svelte';
	import DataFilterSearch from './DataFilterSearch.svelte';

	let selectedFilterOptions = new FilterOptions();
	selectedFilterOptions.politicalParties = ['V', 'S', 'F', 'G', 'N'];

	let legislatureAndMeetings = null;
	let service = new ChartService(); // todo: svelte DI

	const dispatch = createEventDispatcher();

	const triggerSubmit = () => {
		dispatch('submit', selectedFilterOptions);
	};

	// subscribing ONLY to properties is not possible, so we use this workaround
	$: selectedLegislature = selectedFilterOptions.legislature;
	$: selectedLegislature, resetMeetingFilter();

	const resetMeetingFilter = () => {
		if (Array.isArray(legislatureAndMeetings) && legislatureAndMeetings.length) {
			selectedFilterOptions.meetingNumber = legislatureAndMeetings
				.filter((x) => x.legislature == selectedFilterOptions.legislature)[0]
				.meetings.slice(-1)[0];
		}
	};

	onMount(async () => {
		legislatureAndMeetings = await service.getLegislaturesAndMeetings();
		selectedFilterOptions.legislature = legislatureAndMeetings.slice(-1)[0].legislature;
		selectedFilterOptions.meetingNumber = legislatureAndMeetings.slice(-1)[0].meetings.slice(-1)[0];
	});
</script>

<h2 class="card-title">Datenfilter</h2>
{#if legislatureAndMeetings == null}
	<LoadingSpinner />
{:else}

	<DataFilterSelect
		labelText="Gesetzgebungsperiode"
		tooltipText="Nur vollständig digitalisierte Gesetzgebungsperioden sind verfügbar."
		values={legislatureAndMeetings.map((x) => x.legislature)}
		bind:selectedValue={selectedFilterOptions.legislature}
	/>

	<DataFilterSelect
		labelText="Sitzung"
		tooltipText="Nur Sitzungen mit mind. einer kategorisierten Wortmeldungsart sind verfügbar."
		values={legislatureAndMeetings.find((x) => x.legislature === selectedFilterOptions.legislature)?.meetings}
		bind:selectedValue={selectedFilterOptions.meetingNumber}
	/>

	<DataFilterSearch {selectedFilterOptions}></DataFilterSearch>
    
	<div class="relative">
		<label class="block text-gray-700 text-sm font-bold mb-2" for="politicalParty">Fraktion:</label>
		<div
			class="tooltip tooltip-left absolute top-0 right-0"
			data-tip="Vorläufig sind nur derzeit im Parlament aktive Fraktionen verfügbar."
		>
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
		<div class="grid grid-cols-3 gap-2">
			<div class="flex flex-row gap-2 border-2 rounded-full items-center">
				<input
					type="checkbox"
					class="checkbox"
					id="politicalParty_oevp"
					bind:group={selectedFilterOptions.politicalParties}
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
					bind:group={selectedFilterOptions.politicalParties}
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
					bind:group={selectedFilterOptions.politicalParties}
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
					bind:group={selectedFilterOptions.politicalParties}
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
					bind:group={selectedFilterOptions.politicalParties}
					name="NEOS"
					value="N"
				/>
				<label for="politicalParty_neos">NEOS</label>
			</div>
		</div>
	</div>
	<button class="btn" on:click={triggerSubmit}>Grafik aktualisieren</button>
{/if}
