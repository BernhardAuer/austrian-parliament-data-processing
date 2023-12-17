<script>
    export let speech = null;

    const activityMapping = {
        "applause": 
            {emoji: "👏🏻", defaultDescription: "Beifall"},
        "cheerfulness": 
            {emoji: "😅", defaultDescription: "Heiterkeit"},
        "interjectionWithoutQuote": 
            {emoji: "🗣️", defaultDescription: "Zwischenruf"},
    };
</script>

{#if speech?.subtype in activityMapping}
    <div class="flex justify-center items-center">
        <div class="badge badge-outline">
            <div class="tooltip tooltip-secondary" data-tip={speech?.data ?? activityMapping[speech.subtype].defaultDescription}>
                {activityMapping[speech.subtype].emoji} {speech?.nameOfSpeaker}
            </div>
        </div>
    </div>
{:else}
    <!-- default info text / unknown activity -->
    <div class="flex justify-center items-center">
        <div class="badge-accent rounded-lg px-3 py-1">{speech?.data}</div>
    </div>
{/if}