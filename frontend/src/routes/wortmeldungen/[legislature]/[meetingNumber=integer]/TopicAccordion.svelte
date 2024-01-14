<script>
	import SpeechCard from './SpeechCard.svelte';
	import { page } from '$app/stores';
	export let topNr = '';
	export let topic = '';
	export let topicUrlSlug = '';
	export let legislature = '';
	export let meetingNr = null;
	export let speeches = [];
	export let selectedTopicUrlSlug = null;

	const changeSelectedTopic = () => {
		$page.url.searchParams.set('thema', selectedTopicUrlSlug); 
		history.replaceState(history.state, '', $page.url);
	}
</script>

<div class="collapse collapse-arrow bg-base-200">
	<input type="radio" name="thema" checked={selectedTopicUrlSlug == topicUrlSlug} value={topicUrlSlug} bind:group={selectedTopicUrlSlug} on:change={() => changeSelectedTopic()}/>
	<div class="collapse-title text-xl font-medium">{topNr ?? ''} {topic}</div>
	<div class="collapse-content">
		<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4 gap-4 py-4">
			{#each speeches as speech}
				<SpeechCard speech={speech} legislature={legislature} meetingNr={meetingNr} topic={topic}/>
			{/each}
		</div>
	</div>
</div>
