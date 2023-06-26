<script>
    let test = [1,2,3,4,5,6,7,8,9];
</script>

<div class="grid grid-cols-1 md:grid-cols-2 xl:grid-cols-3 2xl:grid-cols-4 gap-4 py-4">

    {#each test as item}
    <div class="card min-w-fit max-w-xs bg-green-50 shadow-xl">
        <div class="card-body"> 
            <h2 class="card-title self-center">Pamela Rendi Wagner</h2>
            <div class="relative flex items-center">
                <div class="flex-grow border-t border-gray-400"></div>
                <span class="flex-shrink mx-4 text-gray-400">SPÖ</span>
                <div class="flex-grow border-t border-gray-400"></div>
            </div> 
           
          <p class="text-justify"> [..] Eigentlich gehen wir oft und gerne davon aus, dass es sich beim Thema Tierschutz um eine Konsensmaterie handelt, dass der Tierschutz allen Parteien im Haus ein großes Anliegen ist und dass die Stimmen der Bevölkerung, die von der Politik mehr 
            Tierwohl einfordern, wie die 427 000 Menschen, die gegen die quälenden Tiertransporte unterschrieben haben, gehört werden. [..]</p>

            <div class="flex flex-wrap self-center gap-2">
                <div class="badge badge-outline">PRO</div>
                <div class="badge badge-outline">10:27 min</div>
                <div class="badge badge-outline">1250 Wörter</div>           
              </div>
        </div>
    </div>
    {/each}    
</div>