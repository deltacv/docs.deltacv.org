export async function onRequest(context) {
  const url = new URL(context.request.url);
  
  // If the user tries to access the fallback .pages.dev URL, seamlessly redirect them instantly
  // to your real, official docs.deltacv.org domain. 
  // This physically prevents anyone from viewing the site on the ugly Cloudflare URL!
  if (url.hostname.endsWith(".pages.dev")) {
    url.hostname = "docs.deltacv.org";
    return Response.redirect(url.toString(), 301);
  }
  
  return context.next();
}
