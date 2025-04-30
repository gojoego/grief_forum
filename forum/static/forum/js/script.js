console.log("✅ JS loaded");

function togglePost(id) {
    const preview = document.getElementById('preview-' + id);
    const body = document.getElementById('body-' + id);

    console.log('🧪 toggle clicked for ID: ', id);
    console.log('preview element: ', preview);
    console.log('body element: ', body)

    if (!preview || !body) {
        console.error('❌ missing preview or body element for ID ', id)
        return;
    }

    const isExpanded = body.style.display === 'block';

    if (isExpanded) {
        body.style.display = 'none';
        preview.style.display = 'block';
        preview.scrollIntoView({ behavior: 'smooth', block: 'start'});
    } else {
        body.style.display = 'block';
        preview.style.display = 'none';
        body.scrollIntoView({ behavior: 'smooth', block: 'start'});        
    }
}

function toggleSection(id){
    const section = document.getElementById(id);
    const button = document.querySelector(`button[onclick="toggleSection('${id}')"]`);

    const isVisible = section.style.display === 'block';
    section.style.display = isVisible ? 'none' : 'block';

    if (button) {
        button.textContent = isVisible
            ? (id === 'about-me' ? 'show about me' : 'show about this website')
            : (id === 'about-me' ? 'hide about me' : 'hide about this website');
    }
}

function showDisclaimerModal(){
    console.log("👀 Checking for disclaimer display...");

    const modal = document.getElementById('disclaimer-modal')
    const continueButton = document.getElementById('continue-button')

    // check if disclaimer already acknowledge this session
    const hasSeenDisclaimer = localStorage.getItem('hasSeenDisclaimer')
    console.log("🧠 localStorage flag:", hasSeenDisclaimer);

    if (!hasSeenDisclaimer && modal && continueButton){
        console.log("📢 Showing modal...");
        modal.style.display = 'flex';

        continueButton.addEventListener('click', function() {
            localStorage.setItem('hasSeenDisclaimer', 'true');
            modal.style.display = 'none';
            console.log("✅ Modal dismissed and localStorage updated.");
        });
    } else {
        console.log("🙌 Disclaimer already acknowledged — forcing modal to stay hidden");
        if (modal) {
            modal.style.display = 'none'
        }
    }
}

document.addEventListener('DOMContentLoaded', showDisclaimerModal);