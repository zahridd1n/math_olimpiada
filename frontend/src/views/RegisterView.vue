<template>
  <div class="register-page">
    <!-- Subtle Mathematical Curves Background -->
    <div class="math-curves-bg" aria-hidden="true">
      <svg class="math-curves-svg animated-wave-1" viewBox="0 0 1440 900" fill="none">
        <path d="M-100 450 C 300 200, 600 700, 1000 350 C 1250 150, 1400 500, 1600 400" stroke="rgba(229, 178, 46, 0.08)" stroke-width="1.5" />
        <path d="M-50 550 C 350 300, 700 800, 1100 450" stroke="rgba(147, 197, 253, 0.05)" stroke-width="1" />
      </svg>
    </div>

    <!-- 1. RO'YXATDAN O'TISH YAKUNLANGAN HOLAT (REGISTRATION CLOSED) -->
    <div v-if="isClosed" class="container register-container closed-container">
      <div class="editorial-card-wrapper closed-card-wrapper">
        <router-link to="/" class="back-link">
          <span class="arrow">←</span> Bosh sahifaga qaytish
        </router-link>

        <!-- Header Status Emblem -->
        <div class="closed-header">
          <div class="closed-emblem-wrap">
            <div class="closed-pulse-ring"></div>
            <div class="closed-emblem-circle">
              <svg viewBox="0 0 24 24" class="closed-svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
                <line x1="16" y1="2" x2="16" y2="6"></line>
                <line x1="8" y1="2" x2="8" y2="6"></line>
                <line x1="3" y1="10" x2="21" y2="10"></line>
                <path d="m9 16 2 2 4-4"></path>
              </svg>
            </div>
          </div>

          <div class="closed-status-pill">
            <span class="pulse-amber-dot"></span>
            <span>QABUL RASMAN YAKUNLANDI</span>
          </div>

          <h1 class="closed-title">
            Olimpiadaga ro'yxatdan o'tish <span class="serif-italic-gold">yakunlandi</span>
          </h1>

          <p class="closed-lead">
            Hurmatli o'quvchilar, ota-onalar va ustozlar! Viloyat matematika olimpiadasida ishtirok etish uchun arizalarni qabul qilish muddati o'z nihoyasiga yetdi. Barcha ro'yxatdan o'tgan nomzodlarga katta qiziqish va faollik uchun samimiy minnatdorchilik bildiramiz!
          </p>
        </div>

        <!-- Informative 4-card grid -->
        <div class="closed-info-grid">
          <div class="closed-info-card">
            <div class="info-card-icon-wrap">
              <svg viewBox="0 0 24 24" class="info-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path>
                <polyline points="14 2 14 8 20 8"></polyline>
                <line x1="16" y1="13" x2="8" y2="13"></line>
                <line x1="16" y1="17" x2="8" y2="17"></line>
                <polyline points="10 9 9 9 8 9"></polyline>
              </svg>
            </div>
            <div class="info-card-body">
              <h2 class="info-card-title">Arizalar ko'rib chiqilmoqda</h2>
              <p class="info-card-desc">Barcha qabul qilingan arizalar saralandi va ishtirokchilarning yakuniy ro'yxati shakllantirildi.</p>
            </div>
          </div>

          <div class="closed-info-card">
            <div class="info-card-icon-wrap">
              <svg viewBox="0 0 24 24" class="info-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <circle cx="12" cy="12" r="10"></circle>
                <polyline points="12 6 12 12 16 14"></polyline>
              </svg>
            </div>
            <div class="info-card-body">
              <h2 class="info-card-title">Olimpiada kuni va vaqti</h2>
              <p class="info-card-desc">Imtihon o'tkaziladigan aniq sana, sinflar kesimidagi vaqtlar rasmiy kanalimiz orqali e'lon qilinadi.</p>
            </div>
          </div>

          <div class="closed-info-card">
            <div class="info-card-icon-wrap">
              <svg viewBox="0 0 24 24" class="info-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                <circle cx="12" cy="10" r="3"></circle>
              </svg>
            </div>
            <div class="info-card-body">
              <h2 class="info-card-title">O'tkazilish manzili</h2>
              <p class="info-card-desc">Farg'ona shahri, Hackathon IT School binosi. Barcha qatnashuvchilar uchun qulay sharoitlar yaratilgan.</p>
            </div>
          </div>

          <div class="closed-info-card">
            <div class="info-card-icon-wrap">
              <svg viewBox="0 0 24 24" class="info-icon" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
              </svg>
            </div>
            <div class="info-card-body">
              <h2 class="info-card-title">SMS va shaxsiy aloqa</h2>
              <p class="info-card-desc">Ro'yxatdan o'tgan har bir ishtirokchining telefon raqamiga sms yoki qo'ng'iroq orqali tasdiq yuboriladi.</p>
            </div>
          </div>
        </div>

        <!-- Official Telegram Channel Card -->
        <div class="telegram-callout-card">
          <div class="callout-inner">
            <div class="callout-tg-badge">
              <svg viewBox="0 0 24 24" class="tg-svg-icon" fill="currentColor">
                <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm4.64 6.8c-.15 1.58-.8 5.42-1.13 7.19-.14.75-.42 1-.68 1.03-.58.05-1.02-.38-1.58-.75-.88-.58-1.38-.94-2.23-1.5-.99-.65-.35-1.01.22-1.59.15-.15 2.71-2.48 2.76-2.69a.2.2 0 00-.05-.18c-.06-.05-.14-.03-.21-.02-.09.02-1.49.95-4.22 2.79-.4.27-.76.41-1.08.4-.36-.01-1.04-.2-1.55-.37-.63-.2-1.12-.31-1.08-.66.02-.18.27-.36.75-.55 2.92-1.27 4.86-2.11 5.83-2.52 2.78-1.16 3.35-1.36 3.73-1.36.08 0 .27.02.39.12.1.08.13.19.14.27-.01.06.01.24 0 .37z"/>
              </svg>
            </div>
            <div class="callout-text">
              <div class="callout-tag">[ TEZKOR YANGILIKLAR ]</div>
              <h3 class="callout-title">Rasmiy Telegram kanalimizni kuzatib boring</h3>
              <p class="callout-desc">Imtihon jadvallari, o'quvchilar ro'yxati va olimpiada natijalari eng birinchi bo'lib rasmiy kanalimizda e'lon qilinadi.</p>
            </div>
            <a :href="siteConfig.social.telegram" target="_blank" rel="noopener noreferrer" class="btn-editorial-pill tg-join-btn">
              <span>Kanalga o'tish</span>
              <span>↗</span>
            </a>
          </div>
        </div>

        <!-- Actions & Contact row -->
        <div class="closed-actions-row">
          <router-link to="/" class="btn-editorial-pill return-btn">
            <span>← Bosh sahifaga qaytish</span>
          </router-link>

          <a :href="siteConfig.contact.phoneLink" class="btn-contact-outline">
            <svg viewBox="0 0 24 24" class="phone-svg" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
              <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
            </svg>
            <span>Aloqa: +998 (50) 045-60-10</span>
          </a>
        </div>

        <!-- Organizer signature -->
        <div class="closed-signature">
          <span>{{ siteConfig.schoolName }}</span>
          <span class="sig-dot">•</span>
          <span>Viloyat matematika olimpiadasi tashkiliy qo'mitasi</span>
        </div>
      </div>
    </div>

    <!-- 2. RO'YXATDAN O'TISH FORMASI (FAOL BO'LGANDA) -->
    <div v-else class="container register-container">
      <div class="editorial-card-wrapper">
        <router-link to="/" class="back-link">
          <span class="arrow">←</span> Bosh sahifaga qaytish
        </router-link>

        <div class="form-header">
          <h1 class="form-title">
            Olimpiadaga <span class="serif-italic-gold">ro'yxatdan</span> <span class="serif-italic">o'tish</span>
          </h1>
          <p class="form-desc">
            Viloyat matematika olimpiadasida qatnashish uchun ma'lumotlaringizni kiriting.
          </p>
        </div>

        <div v-if="serverError" class="error-banner" role="alert">
          {{ serverError }}
        </div>

        <form @submit.prevent="handleSubmit" novalidate class="register-form">
          <!-- Full Name -->
          <div class="form-group" :class="{ error: errors.full_name }">
            <label for="full_name" class="form-label">
              <span>F.I.SH. (O'QUVCHINING TO'LIQ ISMI)</span>
              <span class="required-star">*</span>
            </label>
            <input
              id="full_name"
              v-model="form.full_name"
              type="text"
              class="form-input"
              placeholder="Masalan: Karimov Jasurbek Alisher o'g'li"
              autocomplete="name"
              required
              @blur="validateField('full_name')"
            />
            <span v-if="errors.full_name" class="field-error">{{ errors.full_name }}</span>
          </div>

          <!-- Phone & Class Row -->
          <div class="form-row">
            <div class="form-group" :class="{ error: errors.phone }">
              <label for="phone" class="form-label">
                <span>TELEFON RAQAMI</span>
                <span class="required-star">*</span>
              </label>
              <input
                id="phone"
                v-model="form.phone"
                type="tel"
                class="form-input font-mono"
                placeholder="+998 90 123 45 67"
                autocomplete="tel"
                required
                @blur="validateField('phone')"
                @input="formatPhone"
              />
              <span v-if="errors.phone" class="field-error">{{ errors.phone }}</span>
            </div>

            <div class="form-group" :class="{ error: errors.class_number }">
              <label for="class_number" class="form-label">
                <span>SINF</span>
                <span class="required-star">*</span>
              </label>
              <select
                id="class_number"
                v-model.number="form.class_number"
                class="form-input form-select font-mono"
                required
                @blur="validateField('class_number')"
              >
                <option value="" disabled>Sinfni tanlang</option>
                <option v-for="c in classOptions" :key="c" :value="c">{{ c }}-sinf</option>
              </select>
              <span v-if="errors.class_number" class="field-error">{{ errors.class_number }}</span>
            </div>
          </div>

          <!-- Submit Button -->
          <button
            type="submit"
            class="btn-editorial-pill submit-action"
            :disabled="loading"
          >
            <span v-if="loading" class="spinner"></span>
            <span>{{ submitText }}</span>
            <span v-if="!loading">→</span>
          </button>
        </form>
      </div>
    </div>

    <!-- Success Celebration Modal Notification -->
    <transition name="modal-bounce">
      <div v-if="success" class="modal-backdrop">
        <div class="success-modal-card">
          <!-- Animated checkmark ring -->
          <div class="success-icon-wrap">
            <div class="pulse-ring"></div>
            <div class="icon-circle">
              <svg viewBox="0 0 24 24" class="check-svg" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
                <polyline points="20 6 9 17 4 12"></polyline>
              </svg>
            </div>
          </div>

          <div class="modal-badge">MUVAFFAQIYATLI RO'YXATDAN O'TINGIZ!</div>

          <h2 class="modal-title">
            Tabriklaymiz, arizangiz <span class="gold-text">qabul qilindi!</span>
          </h2>

          <p class="modal-desc">
            Siz viloyat matematika olimpiadasida muvaffaqiyatli ro'yxatdan o'tdingiz. Tez orada koordinatormiz siz bilan bog'lanadi.
          </p>

          <div class="modal-id-box">
            <span class="id-label">ISHTIROKCHI ID RAQAMI</span>
            <span class="id-number font-mono">#{{ participantId }}</span>
          </div>

          <!-- Progress Countdown Bar -->
          <div class="redirect-indicator">
            <span>{{ countdown }} soniyadan so'ng bosh sahifaga yo'naltiriladi...</span>
            <div class="progress-bar-bg">
              <div class="progress-bar-fill" :style="{ width: `${(countdown / 4) * 100}%` }"></div>
            </div>
          </div>

          <button @click="goToHomeImmediately" class="btn-editorial-pill home-redirect-btn">
            <span>Bosh sahifaga o'tish</span>
            <span>→</span>
          </button>
        </div>
      </div>
    </transition>
  </div>
</template>

<script setup>
import { ref, reactive, computed, onMounted, onUnmounted } from "vue"
import { useRoute, useRouter } from "vue-router"
import confetti from "canvas-confetti"
import { registerParticipant } from "../services/api.js"
import { siteConfig } from "../config/site.js"

const route = useRoute()
const router = useRouter()
const classOptions = [5, 6, 7]

// Default to closed as requested by the user
const isClosed = ref(true)

const form = reactive({
  full_name: "",
  phone: "",
  class_number: "",
})

const errors = reactive({})
const loading = ref(false)
const success = ref(false)
const serverError = ref("")
const participantId = ref(null)
const countdown = ref(4)
let timerId = null

onMounted(() => {
  // Admin preview uchun ?open=1 orqali formani ko'rish mumkin
  if (route.query.force === "open" || route.query.open === "1") {
    isClosed.value = false
    document.title = "Olimpiadaga ro'yxatdan o'tish — " + siteConfig.schoolName
  } else {
    isClosed.value = true
    document.title = "Ro'yxatdan o'tish yakunlandi — " + siteConfig.olympiadTitle
  }

  if (route.query.phone) {
    form.phone = route.query.phone
    formatPhone()
  }
})

onUnmounted(() => {
  if (timerId) clearInterval(timerId)
})

const submitText = computed(() => {
  return loading.value ? "Yuborilmoqda..." : "Ro'yxatdan o'tishni yakunlash"
})

function formatPhone() {
  let v = form.phone.replace(/[^\d+]/g, "")
  if (!v.startsWith("+")) {
    if (v.startsWith("998")) v = "+" + v
    else if (v.startsWith("8") || v.startsWith("9")) v = "+998" + v
  }
  form.phone = v
}

function validateField(field) {
  delete errors[field]
  const v = form[field]

  switch (field) {
    case "full_name":
      if (!v || v.trim().length < 3) errors[field] = "To'liq ism-familiyangizni kiriting"
      break
    case "phone":
      if (!v) { errors[field] = "Telefon raqami majburiy"; break }
      {
        const cleaned = v.replace(/[^\d+]/g, "")
        if (!/^\+?998\d{9}$/.test(cleaned)) errors[field] = "Format: +998901234567"
      }
      break
    case "class_number":
      if (!v) errors[field] = "Sinfingizni tanlang"
      break
  }
  return !errors[field]
}

function validateAll() {
  const fields = ["full_name", "phone", "class_number"]
  let valid = true
  for (const f of fields) {
    if (!validateField(f)) valid = false
  }
  return valid
}

function launchCelebration() {
  try {
    confetti({
      particleCount: 80,
      angle: 60,
      spread: 60,
      origin: { x: 0.1, y: 0.7 },
      colors: ['#e5b22e', '#f3cf7a', '#10b981', '#3b82f6', '#ffffff']
    })
    confetti({
      particleCount: 80,
      angle: 120,
      spread: 60,
      origin: { x: 0.9, y: 0.7 },
      colors: ['#e5b22e', '#f3cf7a', '#10b981', '#3b82f6', '#ffffff']
    })
    setTimeout(() => {
      confetti({
        particleCount: 60,
        spread: 100,
        origin: { y: 0.5 },
        colors: ['#e5b22e', '#10b981', '#ffffff']
      })
    }, 250)
  } catch (e) {
    console.log(e)
  }
}

function goToHomeImmediately() {
  if (timerId) clearInterval(timerId)
  router.push("/")
}

async function handleSubmit() {
  serverError.value = ""
  if (!validateAll()) return
  if (loading.value) return

  loading.value = true

  try {
    const payload = {
      full_name: form.full_name.trim(),
      phone: form.phone.replace(/[^\d+]/g, ""),
      class_number: Number(form.class_number),
    }

    const result = await registerParticipant(payload)
    participantId.value = result.id
    success.value = true

    launchCelebration()

    countdown.value = 4
    timerId = setInterval(() => {
      countdown.value--
      if (countdown.value <= 0) {
        clearInterval(timerId)
        router.push("/")
      }
    }, 1000)
  } catch (err) {
    if (err.fieldErrors) {
      for (const [key, msg] of Object.entries(err.fieldErrors)) {
        errors[key] = msg
      }
    }
    serverError.value = err.message || "Xatolik yuz berdi"
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.register-page {
  min-height: 100vh;
  position: relative;
  background-color: var(--bg-deep);
  padding: calc(var(--header-height) + 40px) 0 80px;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

.register-container {
  width: 100%;
  max-width: 620px;
  position: relative;
  z-index: 2;
}

.closed-container {
  max-width: 740px;
}

.editorial-card-wrapper {
  background: rgba(255, 255, 255, 0.025);
  border: 1px solid var(--border-medium);
  border-radius: 20px;
  padding: 44px;
  width: 100%;
  backdrop-filter: blur(16px);
  -webkit-backdrop-filter: blur(16px);
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.4);
}

.closed-card-wrapper {
  padding: 48px 44px;
  background: linear-gradient(180deg, rgba(255, 255, 255, 0.035) 0%, rgba(255, 255, 255, 0.015) 100%);
  border: 1px solid rgba(229, 178, 46, 0.2);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.5), 0 0 50px rgba(229, 178, 46, 0.04);
}

.back-link {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-size: 0.85rem;
  color: var(--text-secondary);
  margin-bottom: 24px;
  transition: color 0.2s ease, transform 0.2s ease;
}

.back-link:hover {
  color: var(--gold);
  transform: translateX(-3px);
}

/* =========================================
   CLOSED STATE STYLES
   ========================================= */
.closed-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-bottom: 34px;
}

.closed-emblem-wrap {
  position: relative;
  width: 76px;
  height: 76px;
  margin-bottom: 20px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.closed-pulse-ring {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid rgba(229, 178, 46, 0.4);
  animation: pulseEffect 2.4s ease-out infinite;
}

.closed-emblem-circle {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(229, 178, 46, 0.2), rgba(217, 158, 43, 0.08));
  border: 1.5px solid var(--gold);
  color: var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 25px rgba(229, 178, 46, 0.25);
}

.closed-svg {
  width: 32px;
  height: 32px;
}

.closed-status-pill {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  background: rgba(229, 178, 46, 0.1);
  border: 1px solid rgba(229, 178, 46, 0.3);
  border-radius: 99px;
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.12em;
  color: var(--gold);
  font-weight: 700;
  margin-bottom: 16px;
}

.pulse-amber-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background-color: var(--gold);
  box-shadow: 0 0 8px var(--gold);
  display: inline-block;
  animation: dotBlink 1.5s ease-in-out infinite;
}

@keyframes dotBlink {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}

.closed-title {
  font-size: clamp(1.85rem, 3.8vw, 2.5rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #ffffff;
  line-height: 1.2;
  margin-bottom: 14px;
}

.closed-lead {
  font-size: 0.98rem;
  color: var(--text-secondary);
  line-height: 1.65;
  max-width: 600px;
  margin: 0 auto;
}

/* Informative 4-card grid */
.closed-info-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
  margin-bottom: 28px;
}

.closed-info-card {
  background: rgba(255, 255, 255, 0.02);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
  padding: 18px;
  display: flex;
  gap: 14px;
  align-items: flex-start;
  transition: all 0.25s ease;
}

.closed-info-card:hover {
  background: rgba(255, 255, 255, 0.04);
  border-color: rgba(229, 178, 46, 0.3);
  transform: translateY(-2px);
}

.info-card-icon-wrap {
  width: 40px;
  height: 40px;
  border-radius: 10px;
  background: rgba(229, 178, 46, 0.08);
  border: 1px solid rgba(229, 178, 46, 0.2);
  color: var(--gold);
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
}

.info-icon {
  width: 20px;
  height: 20px;
}

.info-card-body {
  flex: 1;
}

.info-card-title {
  font-size: 0.92rem;
  font-weight: 600;
  color: #ffffff;
  margin-bottom: 4px;
  letter-spacing: -0.01em;
}

.info-card-desc {
  font-size: 0.82rem;
  color: var(--text-secondary);
  line-height: 1.45;
}

/* Telegram Callout Card */
.telegram-callout-card {
  background: linear-gradient(135deg, rgba(36, 161, 222, 0.12) 0%, rgba(20, 24, 40, 0.7) 100%);
  border: 1px solid rgba(36, 161, 222, 0.3);
  border-radius: 16px;
  padding: 22px 24px;
  margin-bottom: 28px;
  position: relative;
  overflow: hidden;
}

.telegram-callout-card::after {
  content: '';
  position: absolute;
  top: -30px;
  right: -30px;
  width: 100px;
  height: 100px;
  background: radial-gradient(circle, rgba(36, 161, 222, 0.2) 0%, transparent 70%);
  pointer-events: none;
}

.callout-inner {
  display: flex;
  align-items: center;
  gap: 18px;
}

.callout-tg-badge {
  width: 46px;
  height: 46px;
  border-radius: 50%;
  background: #24A1DE;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  flex-shrink: 0;
  box-shadow: 0 4px 16px rgba(36, 161, 222, 0.35);
}

.tg-svg-icon {
  width: 26px;
  height: 26px;
}

.callout-text {
  flex: 1;
}

.callout-tag {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: #53c5f8;
  margin-bottom: 4px;
}

.callout-title {
  font-size: 1rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 4px;
}

.callout-desc {
  font-size: 0.82rem;
  color: var(--text-secondary);
  line-height: 1.45;
}

.tg-join-btn {
  flex-shrink: 0;
  background: #24A1DE !important;
  color: #ffffff !important;
  border-color: #24A1DE !important;
  padding: 10px 18px !important;
  font-size: 0.85rem !important;
  box-shadow: 0 4px 14px rgba(36, 161, 222, 0.3) !important;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.tg-join-btn:hover {
  background: #1e8ec5 !important;
  border-color: #1e8ec5 !important;
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(36, 161, 222, 0.45) !important;
}

/* Actions and contact row */
.closed-actions-row {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 16px;
  margin-bottom: 24px;
  flex-wrap: wrap;
}

.return-btn {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 24px;
  font-size: 0.92rem;
}

.btn-contact-outline {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 12px 20px;
  border-radius: 99px;
  border: 1px solid var(--border-medium);
  background: rgba(255, 255, 255, 0.03);
  color: var(--text-main);
  font-size: 0.88rem;
  font-weight: 500;
  transition: all 0.2s ease;
}

.btn-contact-outline:hover {
  border-color: var(--gold);
  color: var(--gold);
  background: rgba(229, 178, 46, 0.08);
}

.phone-svg {
  width: 16px;
  height: 16px;
  color: var(--gold);
}

.closed-signature {
  text-align: center;
  font-family: var(--font-mono);
  font-size: 0.74rem;
  color: var(--text-dim);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding-top: 18px;
  border-top: 1px solid var(--border-subtle);
}

.sig-dot {
  color: var(--gold);
}

/* =========================================
   FORM STYLES (OPEN STATE)
   ========================================= */
.form-header {
  margin-bottom: 32px;
}

.form-title {
  font-size: clamp(1.8rem, 3.5vw, 2.4rem);
  font-weight: 700;
  letter-spacing: -0.03em;
  color: #ffffff;
  margin-bottom: 8px;
  line-height: 1.2;
}

.form-desc {
  font-size: 0.95rem;
  color: var(--text-secondary);
  line-height: 1.6;
}

/* Error Banner */
.error-banner {
  padding: 14px 18px;
  background: rgba(239, 68, 68, 0.1);
  border: 1px solid rgba(239, 68, 68, 0.3);
  border-radius: 10px;
  margin-bottom: 24px;
  font-size: 0.88rem;
  color: #fca5a5;
}

/* Register Form */
.register-form {
  display: flex;
  flex-direction: column;
  gap: 22px;
}

.form-row {
  display: grid;
  grid-template-columns: 1.2fr 0.8fr;
  gap: 18px;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.form-label {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  font-weight: 600;
  letter-spacing: 0.08em;
  color: var(--text-secondary);
  display: flex;
  align-items: center;
  gap: 4px;
}

.required-star {
  color: var(--gold);
}

.form-input {
  width: 100%;
  height: 50px;
  padding: 0 16px;
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid var(--border-medium);
  border-radius: 10px;
  color: #ffffff;
  font-size: 0.95rem;
  font-family: var(--font-sans);
  transition: all 0.2s ease;
  outline: none;
}

.form-input::placeholder {
  color: var(--text-dim);
  font-size: 0.88rem;
}

.form-input:focus {
  border-color: var(--gold);
  background: rgba(255, 255, 255, 0.06);
  box-shadow: 0 0 18px rgba(229, 178, 46, 0.18);
}

.form-select {
  cursor: pointer;
  appearance: none;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='14' height='14' viewBox='0 0 24 24' fill='none' stroke='%23e5b22e' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpolyline points='6 9 12 15 18 9'%3E%3C/polyline%3E%3C/svg%3E");
  background-repeat: no-repeat;
  background-position: right 14px center;
  padding-right: 36px;
}

.form-select option {
  background-color: var(--bg-section-1);
  color: #ffffff;
}

.field-error {
  font-size: 0.78rem;
  color: #f87171;
  font-family: var(--font-mono);
}

.form-group.error .form-input {
  border-color: #ef4444;
  background: rgba(239, 68, 68, 0.05);
}

.submit-action {
  width: 100%;
  height: 52px;
  font-size: 1rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  margin-top: 10px;
}

.spinner {
  width: 18px;
  height: 18px;
  border: 2px solid rgba(0, 0, 0, 0.2);
  border-top-color: #000000;
  border-radius: 50%;
  animation: spin 0.8s linear infinite;
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

/* Modal styles */
.modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 1000;
  background: rgba(0, 0, 0, 0.82);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.success-modal-card {
  background: linear-gradient(135deg, rgba(20, 16, 38, 0.95), rgba(10, 8, 20, 0.98));
  border: 1px solid rgba(229, 178, 46, 0.4);
  box-shadow: 0 25px 60px rgba(0, 0, 0, 0.7), 0 0 40px rgba(229, 178, 46, 0.2);
  border-radius: 20px;
  padding: 44px 36px;
  max-width: 480px;
  width: 100%;
  text-align: center;
  display: flex;
  flex-direction: column;
  align-items: center;
  animation: modalPop 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}

.success-icon-wrap {
  position: relative;
  width: 76px;
  height: 76px;
  margin-bottom: 22px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pulse-ring {
  position: absolute;
  inset: -6px;
  border-radius: 50%;
  border: 2px solid rgba(16, 185, 129, 0.5);
  animation: pulseEffect 2s ease-out infinite;
}

.icon-circle {
  width: 68px;
  height: 68px;
  border-radius: 50%;
  background: linear-gradient(135deg, #10b981, #059669);
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 0 24px rgba(16, 185, 129, 0.4);
}

.check-svg {
  width: 36px;
  height: 36px;
}

.modal-badge {
  font-family: var(--font-mono);
  font-size: 0.72rem;
  letter-spacing: 0.15em;
  color: #10b981;
  font-weight: 700;
  margin-bottom: 12px;
}

.modal-title {
  font-size: 1.6rem;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 12px;
  line-height: 1.3;
}

.gold-text {
  color: var(--gold);
}

.modal-desc {
  font-size: 0.92rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin-bottom: 24px;
}

.modal-id-box {
  background: rgba(229, 178, 46, 0.08);
  border: 1px solid rgba(229, 178, 46, 0.25);
  border-radius: 12px;
  padding: 14px 28px;
  display: flex;
  flex-direction: column;
  gap: 4px;
  margin-bottom: 24px;
  width: 100%;
}

.id-label {
  font-family: var(--font-mono);
  font-size: 0.68rem;
  letter-spacing: 0.1em;
  color: var(--text-dim);
}

.id-number {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--gold);
}

.redirect-indicator {
  width: 100%;
  margin-bottom: 22px;
  font-size: 0.8rem;
  color: var(--text-dim);
  font-family: var(--font-mono);
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.progress-bar-bg {
  width: 100%;
  height: 4px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 99px;
  overflow: hidden;
}

.progress-bar-fill {
  height: 100%;
  background: var(--gold);
  border-radius: 99px;
  transition: width 1s linear;
}

.home-redirect-btn {
  width: 100%;
  justify-content: center;
  height: 48px;
  font-size: 0.95rem;
}

@keyframes pulseEffect {
  0% {
    transform: scale(0.9);
    opacity: 0.8;
  }
  100% {
    transform: scale(1.4);
    opacity: 0;
  }
}

@keyframes modalPop {
  0% {
    opacity: 0;
    transform: scale(0.9) translateY(20px);
  }
  100% {
    opacity: 1;
    transform: scale(1) translateY(0);
  }
}

.modal-bounce-enter-active,
.modal-bounce-leave-active {
  transition: opacity 0.3s ease;
}

.modal-bounce-enter-from,
.modal-bounce-leave-to {
  opacity: 0;
}

@media (max-width: 680px) {
  .editorial-card-wrapper,
  .closed-card-wrapper {
    padding: 28px 18px;
  }
  .form-row {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .closed-info-grid {
    grid-template-columns: 1fr;
  }
  .callout-inner {
    flex-direction: column;
    text-align: center;
    align-items: center;
  }
  .tg-join-btn {
    width: 100%;
    justify-content: center;
  }
  .closed-actions-row {
    flex-direction: column;
    width: 100%;
  }
  .return-btn,
  .btn-contact-outline {
    width: 100%;
    justify-content: center;
  }
  .success-modal-card {
    padding: 32px 20px;
  }
}
</style>
